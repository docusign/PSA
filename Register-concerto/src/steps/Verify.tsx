import type { StepId } from '../utils/types'
import { StepNav } from '../components/StepNav'

interface Props {
  onNavigate: (step: StepId) => void
}

export function Verify({ onNavigate }: Props) {
  return (
    <div>
      <h2 style={{ marginTop: 0 }}>Verify in Maestro</h2>
      <p>After the API call succeeds, confirm that your model is available in the Maestro UI.</p>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>Verification Steps</h3>
        <ol>
          <li><strong>Open Maestro</strong> in your Docusign account.</li>
          <li><strong>Open or create</strong> the workflow that will use the model.</li>
          <li><strong>Add or configure the "Send Data to CLM" step.</strong></li>
          <li><strong>Open the agreement data model selector</strong> in the step configuration.</li>
          <li><strong>Confirm your registered model appears</strong> in the list of available models.</li>
          <li><strong>Select the model</strong> and configure the fields for your workflow.</li>
        </ol>
      </div>

      <div className="expect">
        <span>✅</span>
        <div>
          <strong>Success:</strong> Your model name and version appear in the data model selector,
          and the fields you defined are available for mapping in the workflow step.
        </div>
      </div>

      <div className="note">
        <span>📝</span>
        <div>
          If the model does not appear, wait a few minutes and refresh. If it still does not show,
          check the Troubleshooting section for common issues.
        </div>
      </div>

      <StepNav currentStep="verify" onNavigate={onNavigate} />
    </div>
  )
}
