"""
Configuration defaults for DocuSign integration.
Copy this file to 'default.py' and replace the placeholder values with your actual credentials.

Steps to get these values:
1. Go to https://admindemo.docusign.com/ > Settings > Apps and Keys
2. Create a new app or use existing one
3. Copy the Integration Key, User ID, Account ID
4. Generate RSA keypair and paste the private key below
"""

# DocuSign API Configuration
INTEGRATION_KEY = '********-****-****-****-************'  # Your DocuSign Integration Key (Client ID)
USER_ID = '********-****-****-****-************'         # Your DocuSign User GUID
ACCOUNT_ID = '********-****-****-****-************'      # Your DocuSign Account GUID
BASE_URI = 'https://demo.docusign.net'                   # DocuSign environment URI (demo or production)

# RSA Private Key (PEM format)
# Generate this from your DocuSign App in Admin panel > Apps and Keys > Actions > Edit > RSA Keypairs
# Copy the entire private key including the BEGIN/END lines
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
PASTE_YOUR_PRIVATE_KEY_HERE
-----END RSA PRIVATE KEY-----"""

# Dropbox Sign API Key
# Get from: https://app.hellosign.com/home/myAccount#api
DROPBOX_SIGN_API_KEY = 'your_dropbox_sign_api_key_here'
