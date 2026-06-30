"""
Configuration settings for Dropbox Sign to DocuSign Migration POC
"""

import os
import sys
from pathlib import Path

# Import configuration from local config/default.py
from config.default import (
    DROPBOX_SIGN_API_KEY,
    INTEGRATION_KEY,
    USER_ID,
    ACCOUNT_ID,
    BASE_URI,
    PRIVATE_KEY
)

# Dropbox Sign Configuration
DROPBOX_SIGN_BASE_URL = "https://api.hellosign.com/v3"
DROPBOX_SIGN_HEADERS = {
    "Authorization": f"Basic {DROPBOX_SIGN_API_KEY}:",
    "Content-Type": "application/json"
}

# Local Storage Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
DOWNLOADS_DIR = TEMPLATES_DIR / "dropbox_sign"

# Create directories if they don't exist
for directory in [TEMPLATES_DIR, DOWNLOADS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Logging Configuration
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "migration.log"

# Migration Settings
MAX_TEMPLATES_PER_PAGE = 20
DEFAULT_TIMEOUT = 30  # seconds
RETRY_ATTEMPTS = 3
RETRY_DELAY = 2  # seconds

# Supported File Formats
SUPPORTED_FORMATS = [
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".html",
    ".xlsx",
    ".xls",
    ".ppt",
    ".pptx",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif"
]

# DocuSign Configuration (for future use)
DOCUSIGN_CONFIG = {
    "integration_key": INTEGRATION_KEY,
    "user_id": USER_ID,
    "account_id": ACCOUNT_ID,
    "base_uri": BASE_URI,
    "private_key": PRIVATE_KEY
}

# UI Configuration
UI_CONFIG = {
    "page_title": "Dropbox Sign → DocuSign Migration",
    "page_icon": "📄",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Status Messages
STATUS_MESSAGES = {
    "connecting": "Connecting to Dropbox Sign API...",
    "connected": "Successfully connected to Dropbox Sign",
    "fetching": "Fetching templates...",
    "downloading": "Downloading template...",
    "downloaded": "Template downloaded successfully",
    "error": "An error occurred. Please check the logs.",
    "no_templates": "No templates found in your Dropbox Sign account"
} 