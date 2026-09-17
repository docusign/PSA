import type { StepId } from '../utils/types'
import { StepNav } from '../components/StepNav'

interface Props {
  onNavigate: (step: StepId) => void
}

export function Troubleshooting({ onNavigate }: Props) {
  return (
    <div>
      <h2 style={{ marginTop: 0 }}>Troubleshooting</h2>
      <p>Common errors you may encounter when registering a Concerto model.</p>

      <table className="table">
        <thead>
          <tr>
            <th style={{ width: 80 }}>Code</th>
            <th>Meaning</th>
            <th>What to Check</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>400</code></td>
            <td>Bad Request</td>
            <td>
              Invalid JSON syntax or invalid model structure. Validate your <code>model-registration.json</code> file.
              Ensure all required fields (<code>$class</code>, <code>namespace</code>, <code>declarations</code>) are present.
            </td>
          </tr>
          <tr>
            <td><code>401</code></td>
            <td>Unauthorized</td>
            <td>
              Missing, expired, or invalid access token. Obtain a fresh token through your organization's OAuth process.
              Verify the <code>Authorization: Bearer</code> header is set correctly.
            </td>
          </tr>
          <tr>
            <td><code>403</code></td>
            <td>Forbidden</td>
            <td>
              Your user account lacks access to this Docusign account or does not have the required
              permission to register models. Contact your account administrator.
            </td>
          </tr>
          <tr>
            <td><code>404</code></td>
            <td>Not Found</td>
            <td>
              Incorrect environment URL, base URL, account ID, or endpoint path. Verify:
              <ul style={{ margin: '4px 0', paddingLeft: 18 }}>
                <li>The base URL matches your environment</li>
                <li>The account ID is correct</li>
                <li>The endpoint path is <code>/v1/accounts/{'{accountId}'}/workflows/models</code></li>
              </ul>
            </td>
          </tr>
          <tr>
            <td><code>409</code></td>
            <td>Conflict</td>
            <td>
              A model with the same namespace and version already exists. Increment the version number
              or delete the existing model before re-registering.
            </td>
          </tr>
          <tr>
            <td><code>429</code></td>
            <td>Rate Limited</td>
            <td>
              Too many requests. Wait a few minutes and try again. Avoid rapid retries.
            </td>
          </tr>
          <tr>
            <td><code>5xx</code></td>
            <td>Server Error</td>
            <td>
              Temporary service or environment issue. Wait and retry. If the error persists, check
              the Docusign status page or contact support.
            </td>
          </tr>
        </tbody>
      </table>

      <div className="card no-hover tint">
        <h3 style={{ marginTop: 0 }}>General Tips</h3>
        <ul>
          <li>Always validate your JSON before sending — use a JSON linter or <code>jq .</code> to check syntax.</li>
          <li>Ensure <code>Content-Type: application/json</code> is set in your request headers.</li>
          <li>Double-check that your token has not expired (tokens are typically short-lived).</li>
          <li>If using a custom environment, verify the base URL is reachable from your network.</li>
          <li>Do not expose or log your <code>Authorization</code> header contents.</li>
        </ul>
      </div>

      <div className="warn">
        <span>⚠️</span>
        <div>
          <strong>Never share authorization headers, tokens, or error responses that contain sensitive data.</strong> Redact
          tokens before sharing logs or screenshots with others.
        </div>
      </div>

      <StepNav currentStep="troubleshooting" onNavigate={onNavigate} />
    </div>
  )
}
