import type { UserConfig, StepId } from '../utils/types'
import { buildCurlCommand } from '../utils/types'
import { CodeBlock } from '../components/CodeBlock'
import { StepNav } from '../components/StepNav'

interface Props {
  config: UserConfig
  onNavigate: (step: StepId) => void
}

export function RegisterCurl({ config, onNavigate }: Props) {
  const curlCmd = buildCurlCommand(config)

  return (
    <div>
      <h2 style={{ marginTop: 0 }}>Register via cURL</h2>
      <p>Use cURL from your terminal to register the model directly.</p>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>1. Set Your Access Token</h3>
        <p>
          Obtain a valid access token through your organization's approved OAuth process, then set
          it as an environment variable in your terminal. <strong>Never paste tokens into URLs or commit them.</strong>
        </p>

        <CodeBlock
          code={`export DOCUSIGN_ACCESS_TOKEN="paste-token-in-terminal-only"`}
          label="macOS / Linux"
        />

        <CodeBlock
          code={`$env:DOCUSIGN_ACCESS_TOKEN = "paste-token-in-terminal-only"`}
          label="Windows PowerShell"
        />
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>2. Run the Registration Command</h3>
        <p>
          Make sure <code>model-registration.json</code> is in your current directory (download it from
          the Convert step), then run:
        </p>
        <CodeBlock code={curlCmd} label="cURL command" />
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>3. Review the Response</h3>
        <p>A successful registration returns a <code>2xx</code> status with the registered model details.</p>
        <div className="expect">
          <span>✅</span>
          <div>
            <strong>Expected:</strong> HTTP 200 or 201 with a JSON body describing the registered model.
          </div>
        </div>
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>4. Clean Up</h3>
        <p>Remove the token from your environment after use:</p>
        <CodeBlock code={`unset DOCUSIGN_ACCESS_TOKEN`} label="macOS / Linux" />
        <CodeBlock code={`Remove-Item Env:DOCUSIGN_ACCESS_TOKEN`} label="Windows PowerShell" />
      </div>

      <div className="warn">
        <span>⚠️</span>
        <div>
          <ul style={{ margin: 0, paddingLeft: 18 }}>
            <li>Do not put the token in the URL.</li>
            <li>Do not commit the token to source control.</li>
            <li>Do not save the token in your repository.</li>
            <li>Remove the environment variable after use.</li>
          </ul>
        </div>
      </div>

      <StepNav currentStep="register-curl" onNavigate={onNavigate} />
    </div>
  )
}
