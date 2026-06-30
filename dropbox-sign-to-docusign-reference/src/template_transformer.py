"""
Template Transformer Service
Converts Dropbox Sign templates to DocuSign template creation payload
"""

import json
import base64
from pathlib import Path
from typing import Dict, List, Any
import sys
import os

from src.auth_manager import DocuSignAuthManager
from config.default import *


class TemplateTransformer:
    """Transform Dropbox Sign templates to DocuSign format"""
    
    def __init__(self):
        # Initialize DocuSign auth manager (reusing from embedded_sign.py)
        self.auth_manager = DocuSignAuthManager(
            integration_key=INTEGRATION_KEY,
            user_id=USER_ID,
            private_key=PRIVATE_KEY,
            base_uri=BASE_URI
        )
        self.account_id = ACCOUNT_ID
        self.base_uri = BASE_URI
    
    def transform_dropbox_to_docusign(self, template_path: str) -> Dict[str, Any]:
        """
        Transform a downloaded Dropbox Sign template to DocuSign format
        
        Args:
            template_path: Path to the template directory containing PDF and API response
            
        Returns:
            DocuSign template creation payload
        """
        template_dir = Path(template_path)
        
        # Load the Dropbox Sign API response
        api_response_file = template_dir / "dropbox_api_response.json"
        with open(api_response_file, 'r') as f:
            dropbox_template = json.load(f)
        
        # Find and read the PDF file
        pdf_file = None
        for file in template_dir.glob("*.pdf"):
            pdf_file = file
            break
        
        if not pdf_file:
            raise FileNotFoundError("No PDF file found in template directory")
        
        # Convert PDF to base64
        with open(pdf_file, 'rb') as f:
            document_base64 = base64.b64encode(f.read()).decode('utf-8')
        
        # Build DocuSign template payload
        docusign_payload = {
            "envelopeTemplateDefinition": {
                "name": dropbox_template.get("title", "Migrated Template"),
                "description": dropbox_template.get("message", "Template migrated from Dropbox Sign"),
                "shared": "false",
                "emailSubject": dropbox_template.get("subject", dropbox_template.get("title", "Please sign this document")),
                "emailBlurb": dropbox_template.get("message", ""),
                "folderName": "Migrated Templates"
            },
            "documents": [
                {
                    "documentId": "1",
                    "name": pdf_file.name,
                    "fileExtension": "pdf",
                    "documentBase64": document_base64
                }
            ],
            "recipients": self._transform_recipients(dropbox_template),
            "status": "created"  # Create as draft first
        }
        
        # Add tabs (form fields) if present
        tabs = self._transform_form_fields(dropbox_template)
        if tabs:
            # Assign tabs to the first signer for now
            if docusign_payload["recipients"].get("signers"):
                docusign_payload["recipients"]["signers"][0]["tabs"] = tabs
        
        return docusign_payload
    
    def _transform_recipients(self, dropbox_template: Dict) -> Dict[str, Any]:
        """Transform Dropbox Sign roles to DocuSign recipients"""
        recipients = {
            "signers": [],
            "carbonCopies": []
        }
        
        # Transform signer roles
        signer_roles = dropbox_template.get("signer_roles", [])
        for index, role in enumerate(signer_roles):
            signer = {
                "recipientId": str(index + 1),
                "routingOrder": str(role.get("order", index + 1)),
                "roleName": role.get("name", f"Signer {index + 1}"),
                "name": "",  # Will be filled when sending
                "email": "",  # Will be filled when sending
                "tabs": {}  # Will be populated with form fields
            }
            recipients["signers"].append(signer)
        
        # If no signers defined, create a default one
        if not recipients["signers"]:
            recipients["signers"].append({
                "recipientId": "1",
                "routingOrder": "1",
                "roleName": "Signer",
                "name": "",
                "email": "",
                "tabs": {}
            })
        
        # Transform CC roles
        cc_roles = dropbox_template.get("cc_roles", [])
        for index, role in enumerate(cc_roles):
            cc = {
                "recipientId": str(len(signer_roles) + index + 1),
                "routingOrder": str(len(signer_roles) + 1),  # CCs usually come after signers
                "roleName": role,
                "name": "",
                "email": ""
            }
            recipients["carbonCopies"].append(cc)
        
        return recipients
    
    def _transform_form_fields(self, dropbox_template: Dict) -> Dict[str, List]:
        """Transform Dropbox Sign form fields to DocuSign tabs"""
        tabs = {
            "signHereTabs": [],
            "initialHereTabs": [],
            "textTabs": [],
            "checkboxTabs": [],
            "dateSignedTabs": [],
            "radioGroupTabs": [],
            "listTabs": []
        }
        
        # Get form fields from Dropbox template
        form_fields = dropbox_template.get("form_fields", [])
        
        for field in form_fields:
            field_type = field.get("type", "")
            
            # Common properties
            base_tab = {
                "documentId": "1",
                "pageNumber": str(field.get("page", 1)),
                "xPosition": str(self._convert_x_coordinate(field.get("x", 0))),
                "yPosition": str(self._convert_y_coordinate(field.get("y", 0))),
                "tabLabel": field.get("name", field.get("api_id", "")),
                "required": str(field.get("required", False)).lower()
            }
            
            # Map field types
            if field_type == "signature":
                tabs["signHereTabs"].append({
                    **base_tab,
                    "scaleValue": 1.0
                })
            
            elif field_type == "initials":
                tabs["initialHereTabs"].append({
                    **base_tab,
                    "scaleValue": 1.0
                })
            
            elif field_type in ["text", "text-single", "text-multi"]:
                text_tab = {
                    **base_tab,
                    "width": str(self._convert_width(field.get("width", 100))),
                    "height": str(self._convert_height(field.get("height", 20))),
                    "value": field.get("value", "")
                }
                tabs["textTabs"].append(text_tab)
            
            elif field_type == "checkbox":
                tabs["checkboxTabs"].append({
                    **base_tab,
                    "selected": str(field.get("value", False)).lower()
                })
            
            elif field_type == "date_signed":
                tabs["dateSignedTabs"].append(base_tab)
            
            elif field_type == "dropdown":
                # Convert dropdown to list tab
                options = field.get("options", [])
                list_items = [{"text": opt, "value": opt} for opt in options]
                
                tabs["listTabs"].append({
                    **base_tab,
                    "listItems": list_items,
                    "value": field.get("value", "")
                })
            
            elif field_type == "radio":
                # Group radio buttons by group name
                group_name = field.get("group", field.get("name", ""))
                
                # Find or create radio group
                radio_group = None
                for group in tabs["radioGroupTabs"]:
                    if group["groupName"] == group_name:
                        radio_group = group
                        break
                
                if not radio_group:
                    radio_group = {
                        "documentId": "1",
                        "groupName": group_name,
                        "radios": []
                    }
                    tabs["radioGroupTabs"].append(radio_group)
                
                # Add radio button to group
                radio_group["radios"].append({
                    "pageNumber": str(field.get("page", 1)),
                    "xPosition": str(self._convert_x_coordinate(field.get("x", 0))),
                    "yPosition": str(self._convert_y_coordinate(field.get("y", 0))),
                    "value": field.get("value", ""),
                    "selected": str(field.get("checked", False)).lower()
                })
        
        # Remove empty tab arrays
        tabs = {k: v for k, v in tabs.items() if v}
        
        return tabs if tabs else None
    
    def _convert_x_coordinate(self, x: int) -> int:
        """Convert Dropbox Sign X coordinate (pixels) to DocuSign (points)"""
        # Dropbox Sign uses pixels, DocuSign uses points
        # 1 pixel = 0.75 points approximately
        return int(x * 0.75)
    
    def _convert_y_coordinate(self, y: int) -> int:
        """Convert Dropbox Sign Y coordinate (pixels) to DocuSign (points)"""
        # Similar conversion, but may need to account for coordinate system differences
        # Dropbox Sign might use top-left origin, DocuSign uses bottom-left
        # This might need adjustment based on page height
        return int(y * 0.75)
    
    def _convert_width(self, width: int) -> int:
        """Convert width from pixels to points"""
        return int(width * 0.75)
    
    def _convert_height(self, height: int) -> int:
        """Convert height from pixels to points"""
        return int(height * 0.75)
    
    def create_template_in_docusign(self, template_path: str) -> Dict[str, Any]:
        """
        Transform and create template in DocuSign
        
        Args:
            template_path: Path to the downloaded Dropbox Sign template
            
        Returns:
            DocuSign API response
        """
        import requests
        
        # Get access token
        access_token = self.auth_manager.get_access_token()
        if not access_token:
            raise Exception("Failed to obtain DocuSign access token")
        
        # Transform template
        payload = self.transform_dropbox_to_docusign(template_path)
        
        # Create template in DocuSign
        url = f"{self.base_uri}/restapi/v2.1/accounts/{self.account_id}/templates"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            result = response.json()
            print(f"✅ Template created successfully in DocuSign!")
            print(f"   Template ID: {result.get('templateId')}")
            print(f"   Template Name: {result.get('name')}")
            return result
        else:
            print(f"❌ Failed to create template: {response.status_code}")
            print(f"   Error: {response.text}")
            raise Exception(f"Failed to create template: {response.text}")


# Example usage
if __name__ == "__main__":
    # Example: Transform a downloaded template
    transformer = TemplateTransformer()
    
    # Path to a downloaded template directory
    template_path = "/Users/ashutosh.shrivastava/Ashutosh-work/E-sign-API/docusign-integration/dropboxsign-to-docusign/templates/dropbox_sign/DemoTemplate_0931d9d4ec3c6dec4bc26de0975dd412d846e939"
    
    # Transform to DocuSign format
    docusign_payload = transformer.transform_dropbox_to_docusign(template_path)
    
    # Print the payload (for debugging)
    print(json.dumps(docusign_payload, indent=2))
    
    # Optionally create in DocuSign
    # result = transformer.create_template_in_docusign(template_path) 