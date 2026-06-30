"""
Dropbox Sign to Docusign Template Migration POC
Flask implementation with modular architecture following existing patterns.
"""

from flask import Flask, render_template_string, request, jsonify, send_file, session
import os
import sys
import json
from pathlib import Path
from datetime import timedelta

# Add parent directory to Python path to import config
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from config.config import *
from src.dropbox_sign_client import DropboxSignClient
from src.template_transformer import TemplateTransformer

app = Flask(__name__)
app.secret_key = 'dropbox-sign-migration-secret-key-2024'  # Change this in production
app.permanent_session_lifetime = timedelta(hours=2)  # Session lasts 2 hours

# Initialize Dropbox Sign client
dropbox_client = DropboxSignClient(DROPBOX_SIGN_API_KEY)

# Store session data (will also use Flask session for persistence)
session_data = {}

@app.route('/')
def index():
    """Main page for template migration."""
    # Check if already connected from session
    is_connected = session.get('connected', False)
    account_info = session.get('account', {})
    
    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dropbox Sign → Docusign Migration</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --inkwell: #130032;
                --cobalt: #4C00FF;
                --deep-violet: #26065D;
                --ecru: #F8F3F0;
                --mist: #CBC2FF;
                --poppy: #FF5252;
                --white: #FFFFFF;
                --grad-atmosphere: linear-gradient(135deg, #CBC2FF, #4C00FF);
                --grad-haze: linear-gradient(135deg, #4C00FF, #26065D);
                --success-green: #00A652;
                --warning-orange: #FF9500;
                --error-red: #FF5252;
                --info-blue: #4C00FF;
                --background: #F8F3F0;
                --card-bg: #FFFFFF;
                --text-primary: #130032;
                --text-secondary: #6C757D;
                --border-color: #E1E4E8;
                --border-light: #F0F2F5;
                --bg-success: #E6F4EA;
                --bg-error: #FFF5F5;
                --bg-info: #EEEAFF;
                --radius: 8px;
                --radius-lg: 12px;
                --shadow-sm: 0 1px 3px rgba(19,0,50,0.06);
                --shadow-md: 0 4px 12px rgba(19,0,50,0.1);
                --shadow-lg: 0 16px 36px rgba(19,0,50,0.12);
            }

            * { margin: 0; padding: 0; box-sizing: border-box; }

            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
                background: linear-gradient(180deg, var(--ecru), var(--white));
                background-attachment: fixed;
                color: var(--text-primary);
                line-height: 1.6;
                min-height: 100vh;
                -webkit-font-smoothing: antialiased;
            }

            .header {
                background: var(--inkwell);
                padding: 20px 0;
                border-bottom: 1px solid rgba(255,255,255,0.06);
            }

            .header-content {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 24px;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }

            .header-brand {
                display: flex;
                align-items: center;
                gap: 12px;
            }

            .header-brand h1 {
                font-size: 18px;
                font-weight: 600;
                color: var(--white);
            }

            .header-brand h1 .source {
                color: var(--mist);
            }

            .header-brand h1 .arrow {
                color: rgba(255,255,255,0.4);
                margin: 0 8px;
                font-size: 14px;
            }

            .header-brand h1 .target {
                color: var(--white);
            }

            .header-subtitle {
                font-size: 13px;
                color: rgba(255,255,255,0.5);
            }

            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 32px 24px;
            }

            .layout {
                display: grid;
                grid-template-columns: 340px 1fr;
                gap: 24px;
            }

            @media (max-width: 860px) {
                .layout { grid-template-columns: 1fr; }
            }

            .card {
                background: var(--card-bg);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-lg);
                box-shadow: var(--shadow-sm);
                overflow: hidden;
            }

            .card-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 16px 20px;
                border-bottom: 1px solid var(--border-color);
                background: var(--ecru);
            }

            .card-title {
                font-size: 14px;
                font-weight: 600;
                color: var(--text-primary);
                display: flex;
                align-items: center;
                gap: 8px;
            }

            .card-title i { color: var(--cobalt); }

            .card-body { padding: 20px; }

            .status-badge {
                display: inline-flex;
                align-items: center;
                gap: 6px;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 500;
            }

            .status-badge.connected { background: var(--bg-success); color: var(--success-green); }
            .status-badge.disconnected { background: var(--bg-error); color: var(--error-red); }
            .status-badge.pending { background: var(--bg-info); color: var(--cobalt); }

            .template-list { max-height: 480px; overflow-y: auto; }

            .template-item {
                padding: 12px 14px;
                border-radius: var(--radius);
                border: 1px solid var(--border-color);
                margin-bottom: 10px;
                cursor: pointer;
                transition: all 0.15s ease;
            }

            .template-item:hover {
                border-color: var(--cobalt);
                background: rgba(76,0,255,0.02);
            }

            .template-item.selected {
                border-color: var(--cobalt);
                background: var(--bg-info);
                box-shadow: 0 0 0 3px rgba(76,0,255,0.08);
            }

            .template-name {
                font-size: 14px;
                font-weight: 600;
                color: var(--text-primary);
                margin-bottom: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
            }

            .template-name i { color: var(--cobalt); font-size: 13px; }

            .template-meta {
                font-size: 12px;
                color: var(--text-secondary);
                display: flex;
                gap: 12px;
                margin-bottom: 4px;
            }

            .template-id {
                font-size: 11px;
                font-family: monospace;
                color: var(--text-secondary);
                background: var(--ecru);
                padding: 2px 6px;
                border-radius: 3px;
                word-break: break-all;
            }

            .spinner {
                width: 32px; height: 32px;
                border: 3px solid var(--border-color);
                border-top-color: var(--cobalt);
                border-radius: 50%;
                animation: spin 0.8s linear infinite;
                margin: 0 auto 12px;
            }

            @keyframes spin { to { transform: rotate(360deg); } }

            .btn {
                padding: 10px 20px;
                font-size: 14px;
                font-weight: 500;
                border: none;
                border-radius: var(--radius);
                cursor: pointer;
                transition: all 0.2s ease;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                text-decoration: none;
            }

            .btn-primary {
                background: var(--cobalt);
                color: var(--white);
            }

            .btn-primary:hover:not(:disabled) {
                background: #5c1aff;
                box-shadow: 0 4px 16px rgba(76,0,255,0.3);
            }

            .btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }

            .btn-secondary {
                background: var(--ecru);
                color: var(--text-primary);
                border: 1px solid var(--border-color);
            }

            .btn-secondary:hover { background: var(--border-light); }

            .btn-sm { padding: 5px 12px; font-size: 12px; }
            .btn-block { width: 100%; }

            .btn-disconnect {
                background: none;
                border: 1px solid rgba(255,255,255,0.2);
                color: rgba(255,255,255,0.6);
                padding: 6px 12px;
                font-size: 12px;
                border-radius: var(--radius);
                cursor: pointer;
                transition: all 0.15s ease;
            }

            .btn-disconnect:hover {
                border-color: var(--poppy);
                color: var(--poppy);
            }

            .tabs {
                display: flex;
                gap: 0;
                border-bottom: 2px solid var(--border-color);
                margin-bottom: 20px;
            }

            .tab {
                padding: 10px 16px;
                font-size: 13px;
                font-weight: 500;
                color: var(--text-secondary);
                border-bottom: 2px solid transparent;
                margin-bottom: -2px;
                cursor: pointer;
                transition: all 0.15s ease;
                display: flex;
                align-items: center;
                gap: 6px;
            }

            .tab:hover { color: var(--text-primary); }

            .tab.active {
                color: var(--cobalt);
                border-bottom-color: var(--cobalt);
                font-weight: 600;
            }

            .tab-panel { display: none; }
            .tab-panel.active { display: block; animation: fadeIn 0.2s ease; }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(4px); }
                to { opacity: 1; transform: translateY(0); }
            }

            .alert {
                padding: 12px 16px;
                border-radius: var(--radius);
                font-size: 13px;
                display: flex;
                align-items: flex-start;
                gap: 10px;
                margin-bottom: 16px;
                border-left: 3px solid;
            }

            .alert i { margin-top: 2px; flex-shrink: 0; }
            .alert-info { background: var(--bg-info); border-color: var(--cobalt); color: var(--cobalt); }
            .alert-success { background: var(--bg-success); border-color: var(--success-green); color: var(--success-green); }
            .alert-danger { background: var(--bg-error); border-color: var(--error-red); color: var(--error-red); }

            .form-group { margin-bottom: 16px; }

            .form-label {
                display: block;
                font-size: 13px;
                font-weight: 600;
                color: var(--text-primary);
                margin-bottom: 6px;
                display: flex;
                align-items: center;
                gap: 6px;
            }

            .form-label i { color: var(--cobalt); font-size: 12px; }

            .form-control {
                width: 100%;
                padding: 10px 14px;
                font-size: 14px;
                font-family: inherit;
                border: 1px solid var(--border-color);
                border-radius: var(--radius);
                background: var(--card-bg);
                color: var(--text-primary);
                transition: border-color 0.2s ease, box-shadow 0.2s ease;
            }

            .form-control:focus {
                outline: none;
                border-color: var(--cobalt);
                box-shadow: 0 0 0 3px rgba(76,0,255,0.1);
            }

            .form-hint {
                font-size: 12px;
                color: var(--text-secondary);
                margin-top: 4px;
            }

            .selected-banner {
                background: var(--grad-haze);
                padding: 16px 20px;
                color: var(--white);
            }

            .selected-banner h4 {
                font-size: 15px;
                font-weight: 600;
                margin-bottom: 6px;
                display: flex;
                align-items: center;
                gap: 8px;
            }

            .selected-banner .meta {
                font-size: 12px;
                opacity: 0.8;
                display: flex;
                align-items: center;
                gap: 12px;
            }

            .selected-banner code {
                font-size: 12px;
                background: rgba(255,255,255,0.15);
                padding: 3px 8px;
                border-radius: 4px;
            }

            .copy-btn {
                background: rgba(255,255,255,0.15);
                border: none;
                color: var(--white);
                padding: 4px 10px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 11px;
                transition: background 0.15s ease;
            }

            .copy-btn:hover { background: rgba(255,255,255,0.25); }

            .empty-state {
                text-align: center;
                padding: 40px 20px;
                color: var(--text-secondary);
            }

            .empty-state i { font-size: 40px; opacity: 0.3; margin-bottom: 12px; display: block; }
        </style>
    </head>
    <body>
        <div class="header">
            <div class="header-content">
                <div class="header-brand">
                    <h1>
                        <span class="source">Dropbox Sign</span>
                        <span class="arrow">→</span>
                        <span class="target">Docusign</span>
                    </h1>
                </div>
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div id="connectionStatus" class="status-badge disconnected">
                        <i class="fas fa-circle" style="font-size: 8px;"></i>
                        <span id="statusText">Not Connected</span>
                    </div>
                    <button id="disconnectBtn" onclick="disconnectFromDropbox()" class="btn-disconnect" style="display: none;">
                        <i class="fas fa-unlink"></i> Disconnect
                    </button>
                </div>
            </div>
        </div>

        <div class="container">
            <div class="layout">
                <!-- Left: Templates Panel -->
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">
                            <i class="fas fa-layer-group"></i>
                            Source Templates
                        </div>
                    </div>
                    <div class="card-body">
                        <div id="connectSection">
                            <button onclick="connectToDropbox()" class="btn btn-primary btn-block" id="connectBtn">
                                <i class="fas fa-plug"></i>
                                Connect to Dropbox Sign
                            </button>
                        </div>

                        <div id="templateSection" style="display: none;">
                            <div id="templateListContainer"></div>
                        </div>

                        <div id="loadingSection" style="display: none;">
                            <div style="text-align: center; padding: 32px;">
                                <div class="spinner"></div>
                                <p style="font-size: 13px; color: var(--text-secondary);">Loading templates...</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right: Migration Panel -->
                <div class="card">
                    <div id="selectedTemplateBanner"></div>
                    <div class="card-header">
                        <div class="card-title">
                            <i class="fas fa-route"></i>
                            Migration Pipeline
                        </div>
                    </div>
                    <div class="card-body">
                        <!-- Tabs -->
                        <div class="tabs">
                            <div class="tab active" data-tab="download"><i class="fas fa-download"></i> Download</div>
                            <div class="tab" data-tab="transform"><i class="fas fa-wand-magic-sparkles"></i> Transform</div>
                            <div class="tab" data-tab="upload"><i class="fas fa-upload"></i> Upload</div>
                            <div class="tab" data-tab="full"><i class="fas fa-rocket"></i> Full Migration</div>
                        </div>

                        <!-- Tab: Download -->
                        <div class="tab-panel active" id="tab-download">
                            <div class="alert alert-info">
                                <i class="fas fa-info-circle"></i>
                                <span><strong>Step 1:</strong> Download template from Dropbox Sign (PDF + metadata + coordinate analysis)</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label"><i class="fas fa-fingerprint"></i> Template ID</label>
                                <input type="text" class="form-control" id="downloadTemplateId" placeholder="Enter Dropbox Sign template ID" style="font-family: monospace;">
                                <div class="form-hint">Select a template from the left panel or paste an ID</div>
                            </div>
                            <button onclick="downloadTemplateById()" class="btn btn-primary btn-block" id="downloadByIdBtn">
                                <i class="fas fa-cloud-download-alt"></i>
                                Download from Dropbox Sign
                            </button>
                            <div id="downloadByIdResult" style="margin-top: 16px; display: none;"></div>
                        </div>

                        <!-- Tab: Transform -->
                        <div class="tab-panel" id="tab-transform">
                            <div class="alert alert-info">
                                <i class="fas fa-info-circle"></i>
                                <span><strong>Step 2:</strong> LLM transforms fields + coordinate system conversion (80 DPI → 72 DPI)</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label"><i class="fas fa-fingerprint"></i> Template ID</label>
                                <input type="text" class="form-control" id="transformTemplateId" placeholder="Previously downloaded template ID" style="font-family: monospace;">
                                <div class="form-hint">Must be a template already downloaded in Step 1</div>
                            </div>
                            <button onclick="transformTemplateById()" class="btn btn-primary btn-block" id="transformByIdBtn">
                                <i class="fas fa-wand-magic-sparkles"></i>
                                Generate Docusign Payload (LLM + Coordinate Fix)
                            </button>
                            <div id="transformByIdResult" style="margin-top: 16px; display: none;"></div>
                        </div>

                        <!-- Tab: Upload -->
                        <div class="tab-panel" id="tab-upload">
                            <div class="alert alert-info">
                                <i class="fas fa-info-circle"></i>
                                <span><strong>Step 3:</strong> Upload the generated payload to create a Docusign template</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label"><i class="fas fa-fingerprint"></i> Template ID</label>
                                <input type="text" class="form-control" id="uploadTemplateId" placeholder="Template ID with payload ready" style="font-family: monospace;">
                                <div class="form-hint">Must have a generated docusign_payload.json from Step 2</div>
                            </div>
                            <button onclick="uploadTemplateById()" class="btn btn-primary btn-block" id="uploadByIdBtn">
                                <i class="fas fa-cloud-upload-alt"></i>
                                Create Template in Docusign
                            </button>
                            <div id="uploadByIdResult" style="margin-top: 16px; display: none;"></div>
                        </div>

                        <!-- Tab: Full Migration -->
                        <div class="tab-panel" id="tab-full">
                            <div class="alert alert-success">
                                <i class="fas fa-bolt"></i>
                                <span><strong>One-Click Migration:</strong> Download → Transform → Upload in a single step</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label"><i class="fas fa-fingerprint"></i> Template ID</label>
                                <input type="text" class="form-control" id="fullTemplateId" placeholder="Dropbox Sign template ID to migrate" style="font-family: monospace;">
                                <div class="form-hint">Runs the complete pipeline end-to-end</div>
                            </div>
                            <button onclick="fullMigrationById()" class="btn btn-primary btn-block" id="fullMigrationBtn">
                                <i class="fas fa-rocket"></i>
                                Run Full Migration
                            </button>
                            <div id="fullMigrationResult" style="margin-top: 16px; display: none;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script>
            let selectedTemplate = null;
            let templates = [];
            let isConnected = {{ 'true' if is_connected else 'false' }};

            // Tab switching
            document.querySelectorAll('.tab').forEach(tab => {
                tab.addEventListener('click', function() {
                    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
                    this.classList.add('active');
                    document.getElementById('tab-' + this.dataset.tab).classList.add('active');
                });
            });

            // Auto-connect on load
            window.addEventListener('DOMContentLoaded', function() {
                if (isConnected) {
                    document.getElementById('connectionStatus').className = 'status-badge connected';
                    document.getElementById('statusText').textContent = 'Connected';
                    document.getElementById('disconnectBtn').style.display = 'inline-flex';
                    document.getElementById('connectSection').style.display = 'none';
                    document.getElementById('loadingSection').style.display = 'block';
                    loadTemplates();
                }
            });

            function connectToDropbox() {
                const btn = document.getElementById('connectBtn');
                const statusBadge = document.getElementById('connectionStatus');
                const statusText = document.getElementById('statusText');

                btn.disabled = true;
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Connecting...';
                statusBadge.className = 'status-badge pending';
                statusText.textContent = 'Connecting...';

                fetch('/connect', { method: 'POST', headers: {'Content-Type': 'application/json'} })
                .then(r => r.json())
                .then(data => {
                    if (data.success) {
                        statusBadge.className = 'status-badge connected';
                        statusText.textContent = 'Connected';
                        document.getElementById('disconnectBtn').style.display = 'inline-flex';
                        document.getElementById('connectSection').style.display = 'none';
                        document.getElementById('loadingSection').style.display = 'block';
                        isConnected = true;
                        loadTemplates();
                    } else {
                        throw new Error(data.error || 'Connection failed');
                    }
                })
                .catch(err => {
                    btn.disabled = false;
                    btn.innerHTML = '<i class="fas fa-plug"></i> Connect to Dropbox Sign';
                    statusBadge.className = 'status-badge disconnected';
                    statusText.textContent = 'Failed';
                    alert('Connection failed: ' + err.message);
                });
            }

            function disconnectFromDropbox() {
                fetch('/disconnect', { method: 'POST', headers: {'Content-Type': 'application/json'} })
                .then(() => window.location.reload());
            }

            function loadTemplates() {
                fetch('/templates').then(r => r.json()).then(data => {
                    if (data.success) {
                        templates = data.templates;
                        displayTemplates(templates);
                        document.getElementById('loadingSection').style.display = 'none';
                        document.getElementById('templateSection').style.display = 'block';
                    } else {
                        throw new Error(data.error);
                    }
                }).catch(err => {
                    document.getElementById('loadingSection').style.display = 'none';
                    alert('Failed to load templates: ' + err.message);
                });
            }

            function displayTemplates(templates) {
                const container = document.getElementById('templateListContainer');
                if (templates.length === 0) {
                    container.innerHTML = '<div class="empty-state"><i class="fas fa-folder-open"></i><p>No templates found</p></div>';
                    return;
                }

                let html = '<div class="template-list">';
                templates.forEach(t => {
                    const signers = t.signer_roles ? t.signer_roles.length : 0;
                    html += `
                        <div class="template-item" onclick="selectTemplate('${t.template_id}')" id="template-${t.template_id}">
                            <div class="template-name"><i class="fas fa-file-contract"></i> ${t.title || 'Untitled'}</div>
                            <div class="template-meta">
                                <span><i class="fas fa-users"></i> ${signers} signers</span>
                            </div>
                            <div class="template-id">${t.template_id}</div>
                        </div>
                    `;
                });
                html += '</div>';
                container.innerHTML = html;
            }

            function selectTemplate(templateId) {
                selectedTemplate = templates.find(t => t.template_id === templateId);
                if (!selectedTemplate) return;

                document.querySelectorAll('.template-item').forEach(i => i.classList.remove('selected'));
                document.getElementById('template-' + templateId).classList.add('selected');

                // Update banner
                const signers = selectedTemplate.signer_roles ? selectedTemplate.signer_roles.length : 0;
                const docs = selectedTemplate.documents ? selectedTemplate.documents.length : 0;
                document.getElementById('selectedTemplateBanner').innerHTML = `
                    <div class="selected-banner">
                        <h4><i class="fas fa-file-contract"></i> ${selectedTemplate.title || 'Untitled'}</h4>
                        <div class="meta">
                            <code>${selectedTemplate.template_id}</code>
                            <button class="copy-btn" onclick="copyId('${selectedTemplate.template_id}')"><i class="fas fa-copy"></i> Copy</button>
                            <span><i class="fas fa-users"></i> ${signers} signers</span>
                            <span><i class="fas fa-file"></i> ${docs} docs</span>
                        </div>
                    </div>
                `;

                // Auto-fill all ID fields
                ['downloadTemplateId','transformTemplateId','uploadTemplateId','fullTemplateId'].forEach(id => {
                    document.getElementById(id).value = selectedTemplate.template_id;
                });
            }

            function copyId(id) {
                navigator.clipboard.writeText(id).catch(() => {
                    const ta = document.createElement('textarea');
                    ta.value = id; document.body.appendChild(ta);
                    ta.select(); document.execCommand('copy');
                    document.body.removeChild(ta);
                });
            }

            function downloadTemplateById() {
                const templateId = document.getElementById('downloadTemplateId').value.trim();
                if (!templateId) { alert('Please enter a template ID'); return; }
                const btn = document.getElementById('downloadByIdBtn');
                const result = document.getElementById('downloadByIdResult');
                result.style.display = 'none';
                btn.disabled = true;
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Downloading...';

                fetch('/download_by_id', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({template_id: templateId}) })
                .then(r => r.json()).then(data => {
                    result.style.display = 'block';
                    result.innerHTML = data.success
                        ? `<div class="alert alert-success"><i class="fas fa-check-circle"></i><span><strong>Downloaded!</strong> ${data.template_name}<br><small>${data.download_path}</small></span></div>`
                        : `<div class="alert alert-danger"><i class="fas fa-exclamation-circle"></i><span><strong>Failed</strong><br>${data.error}</span></div>`;
                    btn.disabled = false;
                    btn.innerHTML = '<i class="fas fa-cloud-download-alt"></i> Download from Dropbox Sign';
                }).catch(err => {
                    result.style.display = 'block';
                    result.innerHTML = `<div class="alert alert-danger"><i class="fas fa-exclamation-circle"></i><span>${err.message}</span></div>`;
                    btn.disabled = false;
                    btn.innerHTML = '<i class="fas fa-cloud-download-alt"></i> Download from Dropbox Sign';
                });
            }

            function transformTemplateById() {
                const templateId = document.getElementById('transformTemplateId').value.trim();
                if (!templateId) { alert('Please enter a template ID'); return; }
                const btn = document.getElementById('transformByIdBtn');
                const result = document.getElementById('transformByIdResult');
                result.style.display = 'none';
                btn.disabled = true;
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Transforming with LLM...';

                fetch('/transform', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({template_id: templateId}) })
                .then(r => r.json()).then(data => {
                    result.style.display = 'block';
                    result.innerHTML = data.success
                        ? `<div class="alert alert-success"><i class="fas fa-check-circle"></i><span><strong>Payload Generated!</strong><br>Template: ${data.template_name}<br>Saved to: ${data.payload_file}<br>Coordinates fixed: ✓</span></div>`
                        : `<div class="alert alert-danger"><i class="fas fa-exclamation-circle"></i><span><strong>Failed</strong><br>${data.error}</span></div>`;
                    btn.disabled = false;
                    btn.innerHTML = '<i class="fas fa-wand-magic-sparkles"></i> Generate Docusign Payload (LLM + Coordinate Fix)';
                }).catch(err => {
                    result.style.display = 'block';
                    result.innerHTML = `<div class="alert alert-danger"><i class="fas fa-exclamation-circle"></i><span>${err.message}</span></div>`;
                    btn.disabled = false;
                    btn.innerHTML = '<i class="fas fa-wand-magic-sparkles"></i> Generate Docusign Payload (LLM + Coordinate Fix)';
                });
            }

            function uploadTemplateById() {
                const templateId = document.getElementById('uploadTemplateId').value.trim();
                if (!templateId) { alert('Please enter a template ID'); return; }
                const btn = document.getElementById('uploadByIdBtn');
                const result = document.getElementById('uploadByIdResult');
                result.style.display = 'none';
                btn.disabled = true;
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Uploading to Docusign...';

                fetch('/upload_to_docusign', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({template_id: templateId}) })
                .then(r => r.json()).then(data => {
                    result.style.display = 'block';
                    result.innerHTML = data.success
                        ? `<div class="alert alert-success"><i class="fas fa-check-circle"></i><span><strong>Template Created in Docusign!</strong><br>Template ID: <code>${data.template_id}</code><br>Name: ${data.template_name}</span></div>`
                        : `<div class="alert alert-danger"><i class="fas fa-exclamation-circle"></i><span><strong>Upload Failed</strong><br>${data.error}</span></div>`;
                    btn.disabled = false;
                    btn.innerHTML = '<i class="fas fa-cloud-upload-alt"></i> Create Template in Docusign';
                }).catch(err => {
                    result.style.display = 'block';
                    result.innerHTML = `<div class="alert alert-danger"><i class="fas fa-exclamation-circle"></i><span>${err.message}</span></div>`;
                    btn.disabled = false;
                    btn.innerHTML = '<i class="fas fa-cloud-upload-alt"></i> Create Template in Docusign';
                });
            }

            function fullMigrationById() {
                const templateId = document.getElementById('fullTemplateId').value.trim();
                if (!templateId) { alert('Please enter a template ID'); return; }
                const btn = document.getElementById('fullMigrationBtn');
                const result = document.getElementById('fullMigrationResult');
                result.style.display = 'none';
                btn.disabled = true;
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Running Full Migration...';

                fetch('/migrate/direct', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({template_id: templateId}) })
                .then(r => r.json()).then(data => {
                    result.style.display = 'block';
                    if (data.success) {
                        let steps = '';
                        if (data.steps) {
                            steps = '<div style="margin-top:8px; font-size:12px;">';
                            if (data.steps.download) steps += '<div>✅ Downloaded from Dropbox Sign</div>';
                            if (data.steps.load) steps += '<div>✅ Template data loaded</div>';
                            if (data.steps.transform) steps += '<div>✅ LLM transformation + coordinate fix</div>';
                            if (data.steps.upload) steps += '<div>✅ Uploaded to Docusign</div>';
                            steps += '</div>';
                        }
                        result.innerHTML = `<div class="alert alert-success"><i class="fas fa-check-circle"></i><span><strong>Migration Successful!</strong><br>Docusign Template ID: <code>${data.template_id}</code><br>Name: ${data.template_name}${steps}</span></div>`;
                    } else {
                        result.innerHTML = `<div class="alert alert-danger"><i class="fas fa-exclamation-circle"></i><span><strong>Migration Failed</strong><br>${data.error}</span></div>`;
                    }
                    btn.disabled = false;
                    btn.innerHTML = '<i class="fas fa-rocket"></i> Run Full Migration';
                }).catch(err => {
                    result.style.display = 'block';
                    result.innerHTML = `<div class="alert alert-danger"><i class="fas fa-exclamation-circle"></i><span>${err.message}</span></div>`;
                    btn.disabled = false;
                    btn.innerHTML = '<i class="fas fa-rocket"></i> Run Full Migration';
                });
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html_template, is_connected=is_connected)

@app.route('/connect', methods=['POST'])
def connect():
    """Test connection to Dropbox Sign API."""
    try:
        result = dropbox_client.test_connection()
        
        if result['success']:
            # Store in both session_data and Flask session for persistence
            session_data['connected'] = True
            session_data['account'] = result['account']
            
            # Store in Flask session for persistence across page refreshes
            session['connected'] = True
            session['account'] = result['account']
            session.permanent = True  # Make session permanent (lasts 2 hours)
            
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/templates')
def get_templates():
    """Get all templates from Dropbox Sign."""
    try:
        # Check if connected first
        if not session.get('connected', False):
            # Try to reconnect
            result = dropbox_client.test_connection()
            if result['success']:
                session['connected'] = True
                session['account'] = result['account']
                session.permanent = True
            else:
                return jsonify({
                    'success': False,
                    'error': 'Not connected to Dropbox Sign',
                    'templates': []
                })
        
        templates = dropbox_client.get_all_templates()
        
        return jsonify({
            'success': True,
            'templates': templates,
            'count': len(templates)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'templates': []
        })

@app.route('/download', methods=['POST'])
def download_template():
    """Download a specific template."""
    try:
        data = request.get_json()
        template_id = data.get('template_id')
        
        if not template_id:
            raise ValueError("Template ID is required")
        
        # Export template for migration
        result = dropbox_client.export_template_for_migration(
            template_id=template_id,
            export_path=DOWNLOADS_DIR
        )
        
        if result['success']:
            # Store in session for later use
            session_data[template_id] = result
            
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/migrate', methods=['POST'])
def migrate_template():
    """Migrate downloaded template to Docusign using modular migrator."""
    try:
        data = request.get_json()
        template_path = data.get('template_path')
        
        if not template_path:
            raise ValueError("Template path is required")
        
        # Extract template ID from path
        import os
        template_id = os.path.basename(template_path).split('_')[-1] if '_' in os.path.basename(template_path) else None
        
        if not template_id:
            raise ValueError("Could not extract template ID from path")
        
        # Use the modular migrator
        from src.template_migrator import TemplateMigrator
        migrator = TemplateMigrator()
        
        # Run step-by-step migration
        result = migrator.migrate_step_by_step(template_id)
        
        if result['success']:
            return jsonify({
                'success': True,
                'template_id': result['template_id'],
                'template_name': result['template_name'],
                'message': 'Template successfully created in Docusign',
                'transformer_type': 'LLM-powered with coordinate fix',
                'steps': result['steps']
            })
        else:
            return jsonify({
                'success': False,
                'error': result.get('error', 'Migration failed'),
                'steps': result.get('steps', {})
            })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/disconnect', methods=['POST'])
def disconnect():
    """Disconnect from Dropbox Sign and clear session."""
    try:
        # Clear Flask session
        session.clear()
        
        # Clear local session data
        session_data.clear()
        
        return jsonify({
            'success': True,
            'message': 'Disconnected successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'Dropbox Sign to Docusign Migration',
        'connected': session.get('connected', False)
            })

@app.route('/download_by_id', methods=['POST'])
def download_by_id():
    """Download a template from Dropbox Sign by template ID."""
    try:
        data = request.get_json()
        template_id = data.get('template_id')
        
        if not template_id:
            raise ValueError("Template ID is required")
        
        # Get template details first
        template_details = dropbox_client.get_template_details(template_id)
        
        if not template_details:
            raise ValueError(f"Template {template_id} not found")
        
        # Create download path - just the base directory, the client will create the template-specific folder
        from pathlib import Path
        download_path = Path("templates/dropbox_sign")
        
        # Download template files (this will create the template-specific subdirectory)
        download_result = dropbox_client.download_template_files(template_id, download_path)
        
        if download_result['success']:
            return jsonify({
                'success': True,
                'template_name': template_details.get('title', 'Untitled'),
                'download_path': str(download_path)
            })
        else:
            return jsonify({
                'success': False,
                'error': download_result.get('error', 'Download failed')
            })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/transform', methods=['POST'])
def transform_template():
    """Transform a downloaded template to Docusign payload."""
    try:
        data = request.get_json()
        template_id = data.get('template_id')
        
        if not template_id:
            raise ValueError("Template ID is required")
        
        from src.template_migrator import TemplateMigrator
        migrator = TemplateMigrator()
        
        # Find the template
        template_path = migrator.find_downloaded_template(template_id)
        if not template_path:
            raise ValueError(f"Template {template_id} not found. Please download it first.")
        
        # Load and transform
        template_data = migrator.load_template_data(template_path)
        docusign_payload = migrator.transform_template(template_data)
        
        # Save the payload
        payload_file = migrator.save_transformed_payload(template_path, docusign_payload)
        
        return jsonify({
            'success': True,
            'template_name': docusign_payload.get('envelopeTemplateDefinition', {}).get('name'),
            'payload_file': payload_file,
            'coordinates_fixed': True
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/upload_to_docusign', methods=['POST'])
def upload_to_docusign():
    """Upload a transformed template to Docusign."""
    try:
        data = request.get_json()
        template_id = data.get('template_id')
        
        if not template_id:
            raise ValueError("Template ID is required")
        
        from src.template_migrator import TemplateMigrator
        import json
        from pathlib import Path
        
        migrator = TemplateMigrator()
        
        # Find the template and payload
        template_path = migrator.find_downloaded_template(template_id)
        if not template_path:
            raise ValueError(f"Template {template_id} not found.")
        
        payload_file = template_path / "docusign_payload.json"
        if not payload_file.exists():
            raise ValueError(f"No payload found. Please transform the template first.")
        
        # Load the payload
        with open(payload_file, 'r') as f:
            payload = json.load(f)
        
        # Upload to Docusign
        result = migrator.upload_to_docusign(payload)
        
        return jsonify({
            'success': True,
            'template_id': result.get('templateId'),
            'template_name': result.get('name')
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/migrate/direct', methods=['POST'])
def migrate_template_direct():
    """Directly migrate a previously downloaded template to Docusign by template ID."""
    try:
        data = request.get_json()
        template_id = data.get('template_id')
        
        if not template_id:
            raise ValueError("Template ID is required")
        
        # Use the modular migrator
        from src.template_migrator import TemplateMigrator
        migrator = TemplateMigrator()
        
        # Run step-by-step migration
        result = migrator.migrate_step_by_step(template_id)
        
        if result['success']:
            return jsonify({
                'success': True,
                'template_id': result['template_id'],
                'template_name': result['template_name'],
                'message': 'Template successfully created in Docusign',
                'transformer_type': 'LLM-powered with coordinate fix',
                'steps': result['steps']
            })
        else:
            return jsonify({
                'success': False,
                'error': result.get('error', 'Migration failed'),
                'steps': result.get('steps', {})
            })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    print("🚀 Starting Dropbox Sign to Docusign Migration Service...")
    print("📄 Templates will be saved to:", DOWNLOADS_DIR)
    print("🌐 Server will be available at: http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001) 