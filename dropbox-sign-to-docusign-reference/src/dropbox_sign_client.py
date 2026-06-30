"""
Dropbox Sign API Client for template management
"""

import requests
import json
import base64
import logging
from typing import Dict, List, Optional, Any
from pathlib import Path
import time
from datetime import datetime
import ssl
import warnings

# Suppress SSL warnings for development
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DropboxSignClient:
    """Client for interacting with Dropbox Sign (HelloSign) API"""
    
    def __init__(self, api_key: str):
        """
        Initialize Dropbox Sign client
        
        Args:
            api_key: Dropbox Sign API key
        """
        self.api_key = api_key
        self.base_url = "https://api.hellosign.com/v3"
        self.session = requests.Session()
        
        # Disable SSL verification for development (corporate proxy/firewall issues)
        # NOTE: In production, use proper SSL certificates
        self.session.verify = False
        
        # Set up authentication
        # Dropbox Sign uses Basic Auth with API key as username and empty password
        auth_string = f"{api_key}:"
        encoded_auth = base64.b64encode(auth_string.encode()).decode()
        
        self.session.headers.update({
            "Authorization": f"Basic {encoded_auth}",
            "Accept": "application/json"
        })
        
        logger.info("Dropbox Sign client initialized (SSL verification disabled for development)")
    
    def test_connection(self) -> Dict[str, Any]:
        """
        Test connection to Dropbox Sign API
        
        Returns:
            Account information if successful
        """
        try:
            response = self.session.get(f"{self.base_url}/account")
            response.raise_for_status()
            
            account_info = response.json().get("account", {})
            logger.info(f"Successfully connected to Dropbox Sign. Account: {account_info.get('email_address')}")
            return {
                "success": True,
                "account": account_info
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to connect to Dropbox Sign: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def list_templates(self, page: int = 1, page_size: int = 20) -> Dict[str, Any]:
        """
        List all templates from Dropbox Sign account
        
        Args:
            page: Page number for pagination
            page_size: Number of templates per page
            
        Returns:
            Dictionary containing templates and pagination info
        """
        try:
            params = {
                "page": page,
                "page_size": page_size
            }
            
            response = self.session.get(
                f"{self.base_url}/template/list",
                params=params
            )
            response.raise_for_status()
            
            data = response.json()
            templates = data.get("templates", [])
            
            # Extract relevant template information
            template_list = []
            for template in templates:
                template_info = {
                    "template_id": template.get("template_id"),
                    "title": template.get("title", "Untitled"),
                    "message": template.get("message", ""),
                    "created_at": template.get("created_at"),
                    "updated_at": template.get("updated_at"),
                    "is_embedded": template.get("is_embedded", False),
                    "can_edit": template.get("can_edit", False),
                    "signer_roles": template.get("signer_roles", []),
                    "cc_roles": template.get("cc_roles", []),
                    "documents": template.get("documents", []),
                    "custom_fields": template.get("custom_fields", []),
                    "named_form_fields": template.get("named_form_fields", {})
                }
                template_list.append(template_info)
            
            result = {
                "success": True,
                "templates": template_list,
                "list_info": data.get("list_info", {}),
                "total_count": data.get("list_info", {}).get("num_results", 0),
                "page": page,
                "page_size": page_size
            }
            
            logger.info(f"Retrieved {len(template_list)} templates from page {page}")
            return result
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to list templates: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "templates": []
            }
    
    def get_template_details(self, template_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific template
        
        Args:
            template_id: ID of the template
            
        Returns:
            Template details
        """
        try:
            response = self.session.get(f"{self.base_url}/template/{template_id}")
            response.raise_for_status()
            
            data = response.json()
            template = data.get("template", {})
            
            # Log the raw response for debugging
            logger.info(f"Retrieved details for template: {template.get('title')}")
            logger.debug(f"Template has {len(template.get('documents', []))} documents")
            
            # Check if form_fields exist and log their structure
            for doc in template.get("documents", []):
                form_fields = doc.get("form_fields", [])
                logger.debug(f"Document {doc.get('name')} has {len(form_fields)} form fields")
                for field in form_fields[:2]:  # Log first 2 fields for debugging
                    logger.debug(f"Field: type={field.get('type')}, x={field.get('x')}, y={field.get('y')}, page={field.get('page', 'NO PAGE PARAM')}")
            
            return {
                "success": True,
                "template": template
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get template details: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def download_template_files(self, template_id: str, download_path: Path) -> Dict[str, Any]:
        """
        Download template files (documents) from Dropbox Sign
        
        Args:
            template_id: ID of the template to download
            download_path: Path to save downloaded files
            
        Returns:
            Download result with file paths
        """
        try:
            # First, get template details to understand the structure
            template_details = self.get_template_details(template_id)
            if not template_details["success"]:
                return template_details
            
            template = template_details["template"]
            template_title = template.get("title", "untitled").replace("/", "_").replace(" ", "_")
            
            # Create template-specific directory
            template_dir = download_path / f"{template_title}_{template_id}"
            template_dir.mkdir(parents=True, exist_ok=True)
            
            downloaded_files = []
            
            # 1. Download template PDF file
            response = self.session.get(
                f"{self.base_url}/template/files/{template_id}",
                params={"file_type": "pdf"}  # Get as PDF for consistency
            )
            
            if response.status_code == 200:
                # Save the template PDF
                file_path = template_dir / f"{template_title}.pdf"
                with open(file_path, "wb") as f:
                    f.write(response.content)
                
                downloaded_files.append(str(file_path))
                logger.info(f"Downloaded template PDF to: {file_path}")
            
            # 2. Save raw API response as JSON (contains everything)
            api_response_path = template_dir / "dropbox_api_response.json"
            with open(api_response_path, "w") as f:
                json.dump(template, f, indent=2, default=str)
            
            downloaded_files.append(str(api_response_path))
            logger.info(f"Saved API response to: {api_response_path}")
            
            # 3. Analyze and save coordinate system info
            coordinate_analysis = {
                "template_id": template_id,
                "template_title": template_title,
                "coordinate_system": "UNKNOWN",
                "dpi": "UNKNOWN",
                "documents": []
            }
            
            for doc in template.get("documents", []):
                doc_info = {
                    "name": doc.get("name"),
                    "form_fields": []
                }
                
                for field in doc.get("form_fields", []):
                    field_info = {
                        "name": field.get("name"),
                        "type": field.get("type"),
                        "x": field.get("x"),
                        "y": field.get("y"),
                        "width": field.get("width"),
                        "height": field.get("height"),
                        "page": field.get("page", "NO_PAGE_PARAM"),
                        "signer": field.get("signer")
                    }
                    doc_info["form_fields"].append(field_info)
                    
                    # Determine coordinate system based on page parameter
                    if field.get("page") is not None:
                        coordinate_analysis["coordinate_system"] = "NEW"
                        coordinate_analysis["dpi"] = "72"
                    else:
                        coordinate_analysis["coordinate_system"] = "OLD"
                        coordinate_analysis["dpi"] = "80"
                
                coordinate_analysis["documents"].append(doc_info)
            
            # Save coordinate analysis
            analysis_path = template_dir / "coordinate_analysis.json"
            with open(analysis_path, "w") as f:
                json.dump(coordinate_analysis, f, indent=2)
            
            downloaded_files.append(str(analysis_path))
            logger.info(f"Saved coordinate analysis to: {analysis_path}")
            logger.info(f"Detected coordinate system: {coordinate_analysis['coordinate_system']} ({coordinate_analysis['dpi']} DPI)")
            
            return {
                "success": True,
                "template_id": template_id,
                "template_title": template_title,
                "download_path": str(template_dir),
                "files": downloaded_files,
                "message": f"Successfully downloaded template to {template_dir}"
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to download template files: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
        except Exception as e:
            logger.error(f"Unexpected error downloading template: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_all_templates(self) -> List[Dict[str, Any]]:
        """
        Get all templates from the account (handles pagination)
        
        Returns:
            List of all templates
        """
        all_templates = []
        page = 1
        page_size = 20
        
        while True:
            result = self.list_templates(page=page, page_size=page_size)
            
            if not result["success"]:
                logger.error(f"Failed to fetch templates on page {page}")
                break
            
            templates = result.get("templates", [])
            all_templates.extend(templates)
            
            # Check if there are more pages
            total_count = result.get("total_count", 0)
            if len(all_templates) >= total_count or len(templates) < page_size:
                break
            
            page += 1
            time.sleep(0.5)  # Rate limiting
        
        logger.info(f"Retrieved total of {len(all_templates)} templates")
        return all_templates
    
    def export_template_for_migration(self, template_id: str, export_path: Path) -> Dict[str, Any]:
        """
        Export template in a format suitable for migration to DocuSign
        Simply downloads the template files - PDF and API response JSON
        
        Args:
            template_id: Template ID to export
            export_path: Path to save exported data
            
        Returns:
            Export result
        """
        try:
            # Just download the template files (PDF + API response JSON)
            download_result = self.download_template_files(template_id, export_path)
            return download_result
            
        except Exception as e:
            logger.error(f"Failed to export template for migration: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            } 