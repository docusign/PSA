import type { UserConfig, StepId, Environment } from '../utils/types'
import { ENVIRONMENT_LABELS } from '../utils/types'
import { StepNav } from '../components/StepNav'

interface Props {
  config: UserConfig
  onChange: (updates: Partial<UserConfig>) => void
  onNavigate: (step: StepId) => void
}

const ENVS: Environment[] = ['demo', 'stage', 'production', 'custom']

export function Prerequisites({ config, onChange, onNavigate }: Props) {
  return (
    <div>
      <h2 style={{ marginTop: 0 }}>Prerequisites</h2>
      <p>Before you begin, make sure you have the following ready.</p>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>Requirements</h3>
        <ol>
          <li>A Docusign account with access to Maestro and CLM</li>
          <li>An OAuth access token obtained through your organization's approved process</li>
          <li>Your account ID (found in the Docusign admin console)</li>
          <li>A Concerto model file (<code>.cto</code>) describing the fields to send to CLM</li>
          <li>One of: Postman, cURL (terminal), or VS Code</li>
        </ol>
      </div>

      <div className="warn">
        <span>⚠️</span>
        <div>
          This guide does <strong>not</strong> ask for your password, OAuth access token, client secret,
          JWT private key, or refresh token. Never enter credentials into this website.
        </div>
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>Configure Your Environment</h3>
        <p>Enter your details below. These are used only to personalize the generated URLs and commands shown in later steps.</p>

        <div className="form-group">
          <label className="form-label" htmlFor="env-select">Environment</label>
          <div className="seg" role="radiogroup" aria-label="Select environment">
            {ENVS.map(env => (
              <button
                key={env}
                className={config.environment === env ? 'active' : ''}
                onClick={() => onChange({ environment: env })}
                role="radio"
                aria-checked={config.environment === env}
              >
                {ENVIRONMENT_LABELS[env]}
              </button>
            ))}
          </div>
        </div>

        {config.environment === 'custom' && (
          <div className="form-group">
            <label className="form-label" htmlFor="custom-url">Custom Base URL</label>
            <input
              id="custom-url"
              className="form-input"
              type="url"
              placeholder="https://your-environment.docusign.net"
              value={config.customBaseUrl}
              onChange={e => onChange({ customBaseUrl: e.target.value })}
            />
          </div>
        )}

        <div className="form-group">
          <label className="form-label" htmlFor="account-id">Account ID</label>
          <input
            id="account-id"
            className="form-input"
            type="text"
            placeholder="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
            value={config.accountId}
            onChange={e => onChange({ accountId: e.target.value })}
          />
          <div className="form-hint">
            Account ID identifies the target account. It is not a login credential.
          </div>
        </div>

        <div className="grid2">
          <div className="form-group">
            <label className="form-label" htmlFor="namespace">Model Namespace</label>
            <input
              id="namespace"
              className="form-input"
              type="text"
              placeholder="DataToCLM"
              value={config.namespace}
              onChange={e => onChange({ namespace: e.target.value })}
            />
          </div>
          <div className="form-group">
            <label className="form-label" htmlFor="version">Model Version</label>
            <input
              id="version"
              className="form-input"
              type="text"
              placeholder="1.0.0"
              value={config.version}
              onChange={e => onChange({ version: e.target.value })}
            />
          </div>
        </div>
      </div>

      <div className="note">
        <span>📝</span>
        <div>
          The model-registration endpoint may vary by environment or API version. Confirm the correct
          endpoint against applicable Docusign documentation before submitting requests in production.
        </div>
      </div>

      <StepNav currentStep="prerequisites" onNavigate={onNavigate} />
    </div>
  )
}
