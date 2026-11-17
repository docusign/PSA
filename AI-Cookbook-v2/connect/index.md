# Connect Docusign

Your admin turns on MCP access once. Then you add the Docusign connector to your AI tool and run a read-only test.

## Steps

1.  Your admin enables MCP access for the account (Admin → Integrations → MCP Connections).
2.  Add the official connector for production, or a custom connector with your Integration Key for demo.
3.  Run the connector test below and confirm a Docusign tool was used.

## Where Docusign connects today

| Platform | Connector | Notes |
| --- | --- | --- |
| **Anthropic Claude** | Official · web, desktop, mobile | Requires Pro, Team or Enterprise (reported). Supports Skills and scheduled tasks. |
| **OpenAI ChatGPT** | Official · app | Requires Pro, Team or Enterprise (reported). |
| **Google Gemini Enterprise** | Official | Requires Gemini Enterprise, Premier or Business (reported). |
| **Microsoft Copilot Studio** | Official · agent tool | Add the connector as a tool in your agent. Plan requirements not found (verify). |
| **Perplexity** | Official | Added after open beta (reported). Plan requirements not found (verify). |
| **Slackbot** | Official | Added after open beta (reported). Plan requirements not found (verify). |
| **Any MCP client** | Custom connector | Use your own Integration Key. Custom agents build their own approval step and request IK allowlisting for production. |

Production

### Official connector

Docusign-maintained, for live accounts. Recommended for everyone.

`https://mcp.docusign.com/mcp`

Demo / build

### Custom connector + IK

For developer accounts with your Integration Key. Demo data only.

`https://mcp-d.docusign.com/mcp`

Admin

### Turn it on or off

Admin → Integrations → MCP Connections. Enforced at the server for every client.

**Labels:** _reported_ means stated by Docusign or a third party but not yet confirmed. _Verify_ means we could not find it, so confirm before relying on it.

**Plan matters.** Maestro (Workflow Builder) and Agreement Manager tools need an active IAM subscription. CLM-backed queries need an eligible CLM and IAM setup. Not yet available for Docusign Government (FedRAMP). English only at GA (reported).

## Test the connector

Step 1 · Test the connector  
**Is Docusign connected? Find out in 30 seconds.**

Run this once before anything else. It only reads, so it is safe on any account.

Use the Docusign connector to list my five most recent envelopes, with status and sent date. Name the Docusign tool you used. Read only: do not send, change or create anything.

Read only**It worked if:** you see a list of your recent envelopes, and your AI tool shows it used a Docusign tool. If your account has no envelopes, the answer says so, and that still proves the connection works. **It did not work if:** no Docusign tool was used. Ask your admin to turn on MCP, or add the Docusign connector in your AI tool, then run it again.

## Go deeper

Official Docusign documentation and blogs. **1P** means Docusign's own agents (Iris and Agent Studio). **3P** means third-party AI tools that connect through MCP.

-   [MCP connectors: Connectors](https://developers.docusign.com/platform/mcp-server/connectors) Production
-   [MCP connectors: Limitations and workarounds](https://developers.docusign.com/platform/mcp-server/limitations-workarounds) Production
-   [Custom connectors: Custom connectors](https://developers.docusign.com/platform/mcp-server/custom-connectors) Developer / demo
-   [Custom connectors: Authentication and scopes](https://developers.docusign.com/platform/mcp-server/authentication-scopes) Developer / demo
-   [Tool reference: MCP tools](https://developers.docusign.com/platform/mcp-server/mcp-tools)
-   [Platform set-up guides: Claude](https://developers.docusign.com/platform/mcp-server/anthropic-claude)
-   [Platform set-up guides: ChatGPT](https://developers.docusign.com/platform/mcp-server/openai-chatgpt)
-   [Platform set-up guides: Copilot Studio](https://developers.docusign.com/platform/mcp-server/microsoft-copilot)
-   [Platform set-up guides: GitHub Copilot](https://developers.docusign.com/platform/mcp-server/github-copilot)
-   [Build agentic agreement workflows](https://www.docusign.com/blog/developers/momentum-26-agentic-agreement-workflows) 1P · Agent Studio
-   [Developer guide to Iris agentic capabilities](https://www.docusign.com/blog/developers/developers-guide-docusign-iris-agentic-capabilities) 1P · Iris
-   [Build agreement agents in Copilot Studio](https://www.docusign.com/blog/build-docusign-agreement-agents-microsoft-copilot-studio) 3P · Via MCP
-   [MCP Server general availability](https://www.docusign.com/blog/developers/docusign-mcp-server-general-availability) 3P · Via MCP
-   [MCP Server for legal AI platforms](https://www.docusign.com/blog/developers/docusign-mcp-server-legal-ai-integration) 3P · Via MCP
-   [Developer guide: Claude connector](https://www.docusign.com/blog/developers/claude-docusign-mcp-connector-guide) 3P · Via MCP

Source: /PSA/AI-Cookbook-v2/connect/
