#!/usr/bin/env python3
"""
Modular Template Migrator
Separates the migration process into distinct steps:
1. Download from Dropbox Sign
2. Transform with LLM + coordinate fix
3. Upload to DocuSign
"""

import os
import json
import base64
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TemplateMigrator:
    """Modular template migrator with separated steps"""
    
    def __init__(self):
        """Initialize the migrator"""
        self.templates_dir = Path("templates/dropbox_sign")
        self.templates_dir.mkdir(parents=True, exist_ok=True)
        
    def find_downloaded_template(self, template_id: str) -> Optional[Path]:
        """
        Find a previously downloaded template by ID
        
        Args:
            template_id: The Dropbox Sign template ID
            
        Returns:
            Path to template directory if found, None otherwise
        """
        for dir_name in os.listdir(self.templates_dir):
            if template_id in dir_name:
                template_path = self.templates_dir / dir_name
                if template_path.exists():
                    # Check if there's a nested directory with the actual files
                    subdirs = [d for d in os.listdir(template_path) if os.path.isdir(template_path / d)]
                    if subdirs:
                        # Return the nested directory that contains the actual files
                        nested_path = template_path / subdirs[0]
                        if (nested_path / "dropbox_api_response.json").exists():
                            return nested_path
                    # Otherwise return the main directory if it has the files
                    if (template_path / "dropbox_api_response.json").exists():
                        return template_path
        return None
    
    def load_template_data(self, template_path: Path) -> Dict[str, Any]:
        """
        Load template data from downloaded files
        
        Args:
            template_path: Path to template directory
            
        Returns:
            Dictionary with template data and PDF base64
        """
        # Load Dropbox Sign API response
        json_file = template_path / "dropbox_api_response.json"
        if not json_file.exists():
            raise FileNotFoundError(f"API response not found: {json_file}")
        
        with open(json_file, 'r') as f:
            dropbox_json = json.load(f)
        
        # Find and load PDF
        pdf_file = None
        for file in os.listdir(template_path):
            if file.endswith('.pdf'):
                pdf_file = template_path / file
                break
        
        if not pdf_file:
            raise FileNotFoundError(f"No PDF found in {template_path}")
        
        with open(pdf_file, 'rb') as f:
            pdf_base64 = base64.b64encode(f.read()).decode('utf-8')
        
        return {
            'dropbox_json': dropbox_json,
            'pdf_base64': pdf_base64,
            'pdf_file': str(pdf_file),
            'template_path': str(template_path)
        }
    
    def transform_template(self, template_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform template using LLM and apply coordinate fixes
        
        Args:
            template_data: Template data from load_template_data
            
        Returns:
            DocuSign payload ready for upload
        """
        import sys
        import os
        # Add parent directory to path for imports
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        from src.llm_transformer import LLMTemplateTransformer
        
        # Initialize transformer WITHOUT DocuSign auth (just for transformation)
        transformer = LLMTemplateTransformer(init_docusign=False)
        
        # Transform with LLM
        print("🤖 Calling LLM for template transformation...")
        docusign_payload = transformer.transform_template(
            template_data['dropbox_json'],
            template_data['pdf_base64']
        )
        
        # The coordinate fix is already applied in transform_template
        print("✅ Transformation complete with coordinate fixes applied")
        
        return docusign_payload
    
    def save_transformed_payload(self, template_path: Path, payload: Dict[str, Any]) -> str:
        """
        Save the transformed payload for review/debugging
        
        Args:
            template_path: Path to template directory
            payload: Transformed DocuSign payload
            
        Returns:
            Path to saved payload file
        """
        output_file = template_path / "docusign_payload.json"
        with open(output_file, 'w') as f:
            json.dump(payload, f, indent=2)
        
        print(f"💾 Saved transformed payload to: {output_file}")
        return str(output_file)
    
    def upload_to_docusign(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Upload the transformed template to DocuSign
        
        Args:
            payload: DocuSign template creation payload
            
        Returns:
            DocuSign API response
        """
        import sys
        import os
        
        from src.auth_manager import DocuSignAuthManager
        from config.config import INTEGRATION_KEY, USER_ID, PRIVATE_KEY, BASE_URI, ACCOUNT_ID
        import requests
        
        # Initialize DocuSign auth
        auth_manager = DocuSignAuthManager(
            integration_key=INTEGRATION_KEY,
            user_id=USER_ID,
            private_key=PRIVATE_KEY,
            base_uri=BASE_URI
        )
        
        # Get access token
        access_token = auth_manager.get_access_token()
        account_id = ACCOUNT_ID  # Use the account ID from config
        
        # Create template in DocuSign
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        url = f"{BASE_URI}/restapi/v2.1/accounts/{account_id}/templates"
        
        print(f"📤 Uploading to DocuSign: {url}")
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            result = response.json()
            print(f"✅ Template created in DocuSign!")
            print(f"   Template ID: {result.get('templateId')}")
            print(f"   Template Name: {result.get('name')}")
            return result
        else:
            error_msg = f"DocuSign API error: {response.status_code} - {response.text}"
            print(f"❌ {error_msg}")
            raise Exception(error_msg)
    
    def migrate_step_by_step(self, template_id: str) -> Dict[str, Any]:
        """
        Migrate template step by step with clear separation
        
        Args:
            template_id: Dropbox Sign template ID
            
        Returns:
            Migration result with all steps
        """
        result = {
            'success': False,
            'steps': {}
        }
        
        try:
            # Step 1: Find or download template
            print(f"\n{'='*60}")
            print("📁 STEP 1: Finding downloaded template...")
            template_path = self.find_downloaded_template(template_id)
            
            if not template_path:
                print(f"⬇️  Template not found locally. Downloading from Dropbox Sign...")
                from src.dropbox_sign_client import DropboxSignClient
                from config.default import DROPBOX_SIGN_API_KEY
                client = DropboxSignClient(DROPBOX_SIGN_API_KEY)
                download_result = client.download_template_files(template_id, Path("templates/dropbox_sign"))
                if download_result.get('success'):
                    template_path = Path(download_result['download_path'])
                    print(f"✅ Downloaded template to: {template_path}")
                    result['steps']['download'] = {'success': True, 'path': str(template_path)}
                else:
                    raise ValueError(f"Failed to download template {template_id}: {download_result.get('error')}")
            else:
                print(f"✅ Found template at: {template_path}")
                result['steps']['download'] = {'success': True, 'path': str(template_path), 'already_downloaded': True}
            
            # Step 2: Load template data
            print(f"\n{'='*60}")
            print("📄 STEP 2: Loading template data...")
            template_data = self.load_template_data(template_path)
            
            print(f"✅ Loaded template: {template_data['dropbox_json'].get('title')}")
            result['steps']['load'] = {'success': True, 'title': template_data['dropbox_json'].get('title')}
            
            # Step 3: Transform with LLM + coordinate fix
            print(f"\n{'='*60}")
            print("🔄 STEP 3: Transforming template...")
            docusign_payload = self.transform_template(template_data)
            
            # Save the payload for debugging
            payload_file = self.save_transformed_payload(template_path, docusign_payload)
            
            result['steps']['transform'] = {
                'success': True, 
                'payload_file': payload_file,
                'template_name': docusign_payload.get('envelopeTemplateDefinition', {}).get('name')
            }
            
            # Step 4: Upload to DocuSign
            print(f"\n{'='*60}")
            print("📤 STEP 4: Uploading to DocuSign...")
            upload_result = self.upload_to_docusign(docusign_payload)
            
            result['steps']['upload'] = {
                'success': True,
                'template_id': upload_result.get('templateId'),
                'template_name': upload_result.get('name')
            }
            
            # Overall success
            result['success'] = True
            result['template_id'] = upload_result.get('templateId')
            result['template_name'] = upload_result.get('name')
            
            print(f"\n{'='*60}")
            print("🎉 MIGRATION SUCCESSFUL!")
            print(f"{'='*60}\n")
            
        except Exception as e:
            print(f"\n❌ Migration failed: {e}")
            result['error'] = str(e)
            import traceback
            traceback.print_exc()
        
        return result


# CLI interface for testing
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python template_migrator.py <template_id>")
        print("Example: python template_migrator.py 0931d9d4ec3c6dec4bc26de0975dd412d846e939")
        sys.exit(1)
    
    template_id = sys.argv[1]
    
    # Run migration
    migrator = TemplateMigrator()
    result = migrator.migrate_step_by_step(template_id)
    
    # Print summary
    if result['success']:
        print("\n✅ Migration completed successfully!")
        print(f"DocuSign Template ID: {result['template_id']}")
        print(f"Template Name: {result['template_name']}")
    else:
        print(f"\n❌ Migration failed: {result.get('error', 'Unknown error')}") 