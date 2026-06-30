# Setup Guide — Dropbox Sign to DocuSign Migration

Complete from-scratch setup when starting with new accounts.

---

## 1. Accounts Required

| Service | URL | What You Need |
|---------|-----|---------------|
| **DocuSign Developer** | https://developers.docusign.com/ | Free developer account |
| **Dropbox Sign** | https://app.hellosign.com/account/signUp | Account with API access |
| **Azure OpenAI** | https://portal.azure.com/ | Azure subscription with OpenAI resource |

---

## 2. DocuSign Setup (JWT Auth)

### 2.1 Create Developer Account
1. Go to https://developers.docusign.com/
2. Sign up for a free developer account
3. After signup, note your **Account ID** (visible in top-right dropdown or Settings)

### 2.2 Create an App (Integration Key)
1. Go to https://admindemo.docusign.com/
2. Navigate to **Settings** → **Apps and Keys**
3. Click **"Add App and Integration Key"**
4. Name it (e.g., "Dropbox Migration POC")
5. Copy the **Integration Key** (this is your Client ID)

### 2.3 Get Your User ID
1. On the same **Apps and Keys** page
2. Your **User ID** (API Username) is displayed at the top — it's a GUID like `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

### 2.4 Generate RSA Keypair
1. In your app settings, under **Service Integration** section
2. Click **"Generate RSA"** 
3. **IMPORTANT:** Copy and save BOTH the private key and public key immediately (you won't see the private key again)
4. The private key goes into `config/default.py`

### 2.5 Grant Consent
This is a **one-time step** required for JWT auth to work:

1. Open this URL in your browser (replace `YOUR_INTEGRATION_KEY`):
   ```
   https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20impersonation&client_id=YOUR_INTEGRATION_KEY&redirect_uri=http://localhost:5001/callback
   ```
2. Log in and click **"Allow Access"**
3. You'll get redirected (the redirect doesn't matter — consent is now granted)

> **Without this step, JWT auth will fail with "consent_required" error.**

### 2.6 Get Account ID
1. Go to **Settings** → **Apps and Keys**
2. Your **API Account ID** is displayed at the top of the page

### 2.7 Values You Need from DocuSign
| Value | Where to Find | Example |
|-------|---------------|---------|
| `INTEGRATION_KEY` | Apps and Keys → Your App | `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |
| `USER_ID` | Apps and Keys → top of page | `12345678-abcd-efgh-ijkl-123456789012` |
| `ACCOUNT_ID` | Apps and Keys → API Account ID | `abcdef12-3456-7890-abcd-ef1234567890` |
| `PRIVATE_KEY` | Generated RSA keypair | Full PEM block |
| `BASE_URI` | Always this for demo | `https://demo.docusign.net` |

---

## 3. Dropbox Sign Setup

### 3.1 Create Account
1. Go to https://app.hellosign.com/account/signUp
2. Sign up (free tier works for API access)

### 3.2 Get API Key
1. Log in to https://app.hellosign.com/
2. Go to **Settings** → **API** (or directly: https://app.hellosign.com/home/myAccount#api)
3. Copy your **API Key**

### 3.3 Create Test Templates (Optional)
1. Go to **Templates** in Dropbox Sign
2. Create a template with signature fields, text fields, etc.
3. This gives you templates to test migration with

### 3.4 Values You Need from Dropbox Sign
| Value | Where to Find |
|-------|---------------|
| `DROPBOX_SIGN_API_KEY` | Settings → API page |

---

## 4. Azure OpenAI Setup

### 4.1 Create Azure OpenAI Resource
1. Go to https://portal.azure.com/
2. Search for **"Azure OpenAI"** → Create
3. Select subscription, resource group, region
4. Name your resource (this becomes part of the endpoint URL)

### 4.2 Deploy GPT-4o Model
1. Go to https://ai.azure.com/ (Azure AI Studio)
2. Select your resource
3. Go to **Deployments** → **Create deployment**
4. Choose **gpt-4o** model
5. Name the deployment (e.g., `gpt-4o`)
6. Note the deployment name

### 4.3 Get Keys & Endpoint
1. In Azure Portal → your OpenAI resource → **Keys and Endpoint**
2. Copy **Key 1** (or Key 2)
3. Copy the **Endpoint** URL

### 4.4 Values You Need from Azure OpenAI
| Value | Where to Find |
|-------|---------------|
| `AZURE_OPENAI_ENDPOINT` | Keys and Endpoint page | 
| `AZURE_OPENAI_API_KEY` | Keys and Endpoint → Key 1 |
| `AZURE_OPENAI_DEPLOYMENT_NAME` | Deployments page (usually `gpt-4o`) |

---

## 5. Configure the Project

### 5.1 Install Dependencies
```bash
cd dropboxsign-to-docusign
pip install -r requirements.txt
```

### 5.2 Create `config/default.py`
```bash
cp config/default.example.py config/default.py
```

Edit `config/default.py` with your actual values:
```python
INTEGRATION_KEY = 'your-integration-key-guid'
USER_ID = 'your-user-id-guid'
ACCOUNT_ID = 'your-account-id-guid'
BASE_URI = 'https://demo.docusign.net'

PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
your-actual-private-key-content-here
-----END RSA PRIVATE KEY-----"""

DROPBOX_SIGN_API_KEY = 'your-dropbox-sign-api-key'
```

### 5.3 Create `.env`
```bash
cp .env.example .env
```

Edit `.env` with your Azure OpenAI values:
```
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
```

---

## 6. Verify Setup

### 6.1 Test DocuSign Auth
```bash
python -c "
from src.auth_manager import DocuSignAuthManager
from config.default import INTEGRATION_KEY, USER_ID, PRIVATE_KEY, BASE_URI
auth = DocuSignAuthManager(INTEGRATION_KEY, USER_ID, PRIVATE_KEY, BASE_URI)
token = auth.get_access_token()
print('SUCCESS - Token:', token[:20] + '...')
"
```

If you get `consent_required` error → go back to Step 2.5 (Grant Consent).

### 6.2 Test Dropbox Sign Connection
```bash
python -c "
from src.dropbox_sign_client import DropboxSignClient
client = DropboxSignClient()
result = client.test_connection()
print(result)
"
```

### 6.3 Test Azure OpenAI
```bash
python -c "
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
load_dotenv()
client = AzureOpenAI(
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    api_version='2024-10-21',
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
)
resp = client.chat.completions.create(
    model='gpt-4o',
    messages=[{'role':'user','content':'Say hello'}],
    max_tokens=10
)
print('SUCCESS:', resp.choices[0].message.content)
"
```

### 6.4 Run the App
```bash
python app.py
```
Open http://localhost:5001

---

## 7. Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `consent_required` | JWT consent not granted | Do Step 2.5 — open consent URL in browser |
| `invalid_grant` | Wrong User ID or Integration Key | Double-check GUIDs in config/default.py |
| `ACCOUNT_DOES_NOT_EXIST` | Wrong Account ID | Get correct API Account ID from Apps and Keys |
| `401 Unauthorized` (Dropbox) | Bad API key | Regenerate key at hellosign.com/home/myAccount#api |
| `openai.AuthenticationError` | Bad Azure key or endpoint | Check .env values match Azure Portal |
| `DeploymentNotFound` | Wrong deployment name | Check actual deployment name in Azure AI Studio |
| `ModuleNotFoundError: config.default` | Missing config file | Run `cp config/default.example.py config/default.py` |

---

## 8. Files Checklist

After setup, your project should have:

```
dropboxsign-to-docusign/
├── .env                    ← Azure OpenAI keys (DO NOT commit)
├── config/
│   ├── config.py           ← App config (reads from default.py)
│   └── default.py          ← Your credentials (DO NOT commit)
├── src/
│   ├── auth_manager.py     ← DocuSign JWT auth
│   ├── dropbox_sign_client.py
│   ├── llm_transformer.py
│   ├── template_migrator.py
│   └── template_transformer.py
└── app.py
```

**Never commit:** `config/default.py`, `.env`
