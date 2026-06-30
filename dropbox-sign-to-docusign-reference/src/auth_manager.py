"""
DocuSign Authentication Manager
Handles JWT token generation and caching for DocuSign API access.
"""

import time
import requests
from datetime import datetime, timedelta
import jwt  # Using PyJWT instead of python-jose
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


class DocuSignAuthManager:
    """
    Manages DocuSign authentication using JWT Grant flow.
    Handles token generation, caching, and refresh.
    """
    
    def __init__(self, integration_key, user_id, private_key, base_uri='https://demo.docusign.net'):
        """
        Initialize the authentication manager.
        
        Args:
            integration_key (str): DocuSign Integration Key (Client ID)
            user_id (str): DocuSign User ID (GUID)
            private_key (str): RSA Private Key in PEM format
            base_uri (str): DocuSign base URI (default: demo environment)
        """
        self.integration_key = integration_key
        self.user_id = user_id
        self.private_key = self._format_private_key(private_key)
        self.base_uri = base_uri
        self.base_path = base_uri + '/restapi'
        self.oauth_base_url = 'https://account-d.docusign.com/oauth/token'
        
        # Token caching
        self.cached_access_token = None
        self.token_expiration_time = None
    
    def _format_private_key(self, private_key_str):
        """
        Format the private key string to ensure proper PEM format.
        
        Args:
            private_key_str (str): Private key string
            
        Returns:
            bytes: Properly formatted private key bytes
        """
        # If it's already properly formatted, return as bytes
        if '-----BEGIN RSA PRIVATE KEY-----' in private_key_str and '\n' in private_key_str:
            return private_key_str.encode('utf-8')
        
        # If it's a single line, add proper newlines
        lines = private_key_str.replace('-----BEGIN RSA PRIVATE KEY-----', '').replace('-----END RSA PRIVATE KEY-----', '').strip()
        
        # Split into 64-character lines
        formatted_lines = []
        for i in range(0, len(lines), 64):
            formatted_lines.append(lines[i:i+64])
        
        # Reconstruct with proper headers and newlines
        formatted_key = "-----BEGIN RSA PRIVATE KEY-----\n" + "\n".join(formatted_lines) + "\n-----END RSA PRIVATE KEY-----"
        return formatted_key.encode('utf-8')
    
    def get_access_token(self):
        """
        Get a valid access token, using cached token if available and not expired.
        
        Returns:
            str: Valid access token
        """
        # Check if cached token is still valid (with 5-minute buffer)
        if (self.cached_access_token and 
            self.token_expiration_time and 
            datetime.now() < self.token_expiration_time - timedelta(minutes=5)):
            print("🔑 Using cached access token")
            return self.cached_access_token
        
        print("🔑 Generating new access token via JWT...")
        return self._generate_jwt_token()
    
    def get_account_id(self):
        """Get the account ID from config"""
        from config.config import ACCOUNT_ID
        return ACCOUNT_ID
    
    def _generate_jwt_token(self):
        """
        Generate a new JWT token and exchange it for an access token.
        
        Returns:
            str: Access token
            
        Raises:
            Exception: If token generation fails
        """
        try:
            # Load the private key
            private_key = serialization.load_pem_private_key(
                self.private_key,
                password=None,
                backend=default_backend()
            )
            
            # JWT Claims
            now = int(time.time())
            claims = {
                "iss": self.integration_key,
                "sub": self.user_id,
                "aud": "account-d.docusign.com",
                "scope": "signature impersonation",
                "iat": now,
                "exp": now + 3600  # 1 hour
            }
            
            # Generate JWT using PyJWT
            jwt_token = jwt.encode(
                claims,
                private_key,
                algorithm="RS256"
            )
            
            print(f"✅ JWT token generated successfully")
            
            # Exchange JWT for access token
            return self._exchange_jwt_for_access_token(jwt_token)
            
        except Exception as e:
            raise Exception(f"Error generating access token: {e}")
    
    def _exchange_jwt_for_access_token(self, jwt_token):
        """
        Exchange JWT token for DocuSign access token.
        
        Args:
            jwt_token (str): JWT token
            
        Returns:
            str: Access token
        """
        try:
            # Prepare the request
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            data = {
                'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
                'assertion': jwt_token
            }
            
            # Make the request
            response = requests.post(self.oauth_base_url, headers=headers, data=data)
            
            if response.status_code == 200:
                token_data = response.json()
                access_token = token_data['access_token']
                expires_in = token_data.get('expires_in', 3600)
                
                # Cache the token
                self.cached_access_token = access_token
                self.token_expiration_time = datetime.now() + timedelta(seconds=expires_in)
                
                print(f"✅ Access token obtained successfully (expires in {expires_in}s)")
                return access_token
            else:
                raise Exception(f"Token exchange failed: {response.status_code} - {response.text}")
                
        except Exception as e:
            raise Exception(f"Error exchanging JWT for access token: {e}")
