import type { UserConfig, StepId } from '../utils/types'
import { buildCurlCommand } from '../utils/types'
import { CodeBlock } from '../components/CodeBlock'
import { StepNav } from '../components/StepNav'

interface Props {
  config: UserConfig
  onNavigate: (step: StepId) => void
}

export function RegisterVSCode({ config, onNavigate }: Props) {
  const ns = config.namespace || 'DataToCLM'
  const ver = config.version || '1.0.0'
  const curlCmd = buildCurlCommand(config)

  const modelCto = `namespace ${ns}@${ver}

concept ${ns} {
  o String EnvelopeId
}`

  return (
    <div>
      <h2 style={{ marginTop: 0 }}>Register via VS Code / Terminal</h2>
      <p>A local workflow for developers who prefer working in VS Code.</p>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>1. Save the Model File</h3>
        <p>Create a file named <code>model.cto</code> with your Concerto model:</p>
        <CodeBlock code={modelCto} label="model.cto" />
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>2. Convert to JSON</h3>
        <p>
          Convert <code>model.cto</code> to <code>model-registration.json</code> using the Concerto CLI
          or the prepared JSON template from the Convert step.
        </p>
        <CodeBlock
          code="npx @accordproject/concerto-cli compile --model model.cto --target JSONSchema"
          label="Using Concerto CLI"
        />
        <p>Or download the pre-built JSON from the Convert step and save it as <code>model-registration.json</code>.</p>
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>3. Open the Terminal in VS Code</h3>
        <p>
          Press <code>Ctrl+`</code> (or <code>Cmd+`</code> on macOS) to open the integrated terminal.
          Navigate to the directory containing <code>model-registration.json</code>.
        </p>
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>4. Set the Access Token</h3>
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
        <h3 style={{ marginTop: 0 }}>5. Run the cURL Command</h3>
        <CodeBlock code={curlCmd} label="Registration request" />
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>6. Review the Response</h3>
        <div className="expect">
          <span>✅</span>
          <div>
            <strong>Expected:</strong> HTTP 200 or 201 with a JSON body confirming the model registration.
          </div>
        </div>
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>7. Clean Up and Verify</h3>
        <CodeBlock code="unset DOCUSIGN_ACCESS_TOKEN" label="Remove token (macOS/Linux)" />
        <CodeBlock code="Remove-Item Env:DOCUSIGN_ACCESS_TOKEN" label="Remove token (PowerShell)" />
        <p>Then verify the model in Maestro (next step).</p>
      </div>

      <StepNav currentStep="register-vscode" onNavigate={onNavigate} />
    </div>
  )
}
