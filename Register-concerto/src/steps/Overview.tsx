import type { UserConfig } from '../utils/types'
import { StepNav } from '../components/StepNav'
import type { StepId } from '../utils/types'

interface Props {
  config: UserConfig
  onNavigate: (step: StepId) => void
}

export function Overview({ onNavigate }: Props) {
  return (
    <div>
      <div className="hero">
        <div className="lbl">Docusign Platform</div>
        <h1>Concerto Model Registration Guide</h1>
        <p>
          Learn how to define, convert, and register a Concerto data model with your Docusign account
          so that Maestro workflows can send structured data to CLM.
        </p>
      </div>

      <div className="card no-hover">
        <h2 style={{ marginTop: 0 }}>What is Concerto Model Registration?</h2>
        <p>
          Concerto model registration is the process of making a data model available to the Maestro
          "Send Data to CLM" workflow step. It involves four actions:
        </p>
        <ol>
          <li><strong>Define a Concerto data model</strong> — describe the fields your workflow will send to CLM.</li>
          <li><strong>Convert the <code>.cto</code> model to Concerto metamodel JSON</strong> — the API accepts the metamodel format, not raw Concerto syntax.</li>
          <li><strong>Submit the JSON to the account-scoped Maestro API endpoint</strong> — a manual POST request that registers the model in your account.</li>
          <li><strong>Use the registered model in Maestro</strong> — select it in the "Send Data to CLM" step configuration.</li>
        </ol>
      </div>

      <div className="card no-hover tint">
        <h3 style={{ marginTop: 0 }}>What registration does NOT do</h3>
        <ul>
          <li>Create a Docusign account</li>
          <li>Enable IAM or configure authentication</li>
          <li>Create a Maestro workflow</li>
          <li>Map fields between systems</li>
          <li>Populate data in CLM</li>
        </ul>
        <p>
          Registration only makes the model <em>available</em> as a schema that Maestro can reference.
          The workflow itself handles data flow.
        </p>
      </div>

      <div className="info-block">
        <span>ℹ️</span>
        <div>
          <strong>This tool is instructional only.</strong> It does not log you in, collect tokens, or
          make API calls. It generates step-by-step instructions and commands that you execute manually
          using your own approved Docusign authentication.
        </div>
      </div>

      <StepNav currentStep="overview" onNavigate={onNavigate} />
    </div>
  )
}
