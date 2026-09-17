import type { UserConfig, StepId } from '../utils/types'
import { buildModelJson } from '../utils/types'
import { CodeBlock } from '../components/CodeBlock'
import { DownloadButton } from '../components/DownloadButton'
import { StepNav } from '../components/StepNav'

interface Props {
  config: UserConfig
  onNavigate: (step: StepId) => void
}

export function ConvertModel({ config, onNavigate }: Props) {
  const modelJson = buildModelJson(config)

  return (
    <div>
      <h2 style={{ marginTop: 0 }}>Convert the Model to JSON</h2>
      <p>
        The Maestro API accepts Concerto metamodel JSON, not raw <code>.cto</code> syntax.
        You must convert your model before registration.
      </p>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>Option A — Use the Concerto CLI or Package</h3>
        <p>
          If you have the <code>@accordproject/concerto-tools</code> package installed, you can convert
          programmatically:
        </p>
        <CodeBlock
          code={`npx @accordproject/concerto-cli compile --model model.cto --target JSONSchema`}
          label="Using the Concerto CLI"
        />
        <p>
          Refer to the <a href="https://concerto.accordproject.org/" target="_blank" rel="noopener noreferrer">
          Concerto documentation</a> for full conversion options and validation.
        </p>
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>Option B — Use the Prepared JSON Template</h3>
        <p>
          Below is the metamodel JSON for your configured model. This is an <strong>example template</strong> —
          validate it against your actual model before submitting.
        </p>
        <CodeBlock code={modelJson} label="model-registration.json" />
        <div style={{ marginTop: 12, display: 'flex', gap: 10 }}>
          <DownloadButton
            content={modelJson}
            filename="model-registration.json"
            label="Download model-registration.json"
          />
        </div>
      </div>

      <div className="warn">
        <span>⚠️</span>
        <div>
          <strong>Important:</strong> The JSON template above is a simplified example based on
          your namespace and version settings. If your model has additional fields or complex types,
          you must update the <code>properties</code> array accordingly or use Option A for a complete conversion.
        </div>
      </div>

      <div className="note">
        <span>📝</span>
        <div>
          An older or internal registration form may use a <code>/declarations</code> endpoint
          instead of <code>/models</code>. Do not treat these as interchangeable without confirming
          which endpoint your environment expects.
        </div>
      </div>

      <StepNav currentStep="convert-model" onNavigate={onNavigate} />
    </div>
  )
}
