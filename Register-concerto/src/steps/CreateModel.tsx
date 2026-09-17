import type { UserConfig, StepId } from '../utils/types'
import { DEFAULT_CTO } from '../utils/types'
import { CodeBlock } from '../components/CodeBlock'
import { DownloadButton } from '../components/DownloadButton'
import { StepNav } from '../components/StepNav'

interface Props {
  config: UserConfig
  onChange: (updates: Partial<UserConfig>) => void
  onNavigate: (step: StepId) => void
}

export function CreateModel({ config, onChange, onNavigate }: Props) {
  const ns = config.namespace || 'DataToCLM'
  const ver = config.version || '1.0.0'
  const displayModel = config.ctoModel || DEFAULT_CTO

  const customizedModel = `namespace ${ns}@${ver}

concept ${ns} {
  o String EnvelopeId
}`

  return (
    <div>
      <h2 style={{ marginTop: 0 }}>Create a Concerto Model</h2>
      <p>
        A Concerto model defines the fields that a Maestro workflow will send back to CLM via the
        "Send Data to CLM" step. Each field in the model becomes an available data point in the workflow.
      </p>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>Sample Model</h3>
        <p>Below is a minimal example with a single <code>EnvelopeId</code> field:</p>
        <CodeBlock code={customizedModel} label="model.cto" />
        <div style={{ marginTop: 12, display: 'flex', gap: 10 }}>
          <DownloadButton
            content={customizedModel}
            filename="model.cto"
            label="Download model.cto"
            mime="text/plain"
          />
        </div>
      </div>

      <div className="card no-hover tint">
        <h3 style={{ marginTop: 0 }}>Customize Your Model</h3>
        <p>
          Add additional fields to match what your workflow needs to send to CLM.
          Common field types include <code>String</code>, <code>Integer</code>,
          <code>DateTime</code>, and <code>Boolean</code>.
        </p>
        <CodeBlock
          code={`namespace ${ns}@${ver}

concept ${ns} {
  o String EnvelopeId
  o String RecipientName optional
  o String RecipientEmail optional
  o DateTime SignedDate optional
}`}
          label="Extended example"
        />
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>Edit Your Model (Optional)</h3>
        <p>Paste or edit your own <code>.cto</code> model below. This will be used in the conversion step.</p>
        <div className="form-group">
          <textarea
            className="form-input"
            value={displayModel}
            onChange={e => onChange({ ctoModel: e.target.value })}
            placeholder="Paste your .cto model here..."
            aria-label="Concerto model editor"
          />
        </div>
      </div>

      <div className="note">
        <span>📝</span>
        <div>
          The model should contain only the fields that the Maestro workflow will send back to CLM.
          You do not need to include fields handled by other workflow steps.
        </div>
      </div>

      <StepNav currentStep="create-model" onNavigate={onNavigate} />
    </div>
  )
}
