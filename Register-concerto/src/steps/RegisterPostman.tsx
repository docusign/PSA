import type { UserConfig, StepId } from '../utils/types'
import { getRegistrationUrl, buildModelJson, buildPostmanCollection } from '../utils/types'
import { CodeBlock } from '../components/CodeBlock'
import { DownloadButton } from '../components/DownloadButton'
import { StepNav } from '../components/StepNav'

interface Props {
  config: UserConfig
  onNavigate: (step: StepId) => void
}

export function RegisterPostman({ config, onNavigate }: Props) {
  const regUrl = getRegistrationUrl(config)
  const modelJson = buildModelJson(config)
  const collection = buildPostmanCollection(config)

  return (
    <div>
      <h2 style={{ marginTop: 0 }}>Register via Postman</h2>
      <p>Follow these steps to register your model using Postman.</p>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>Quick Start — Import Collection</h3>
        <p>Download the pre-configured Postman collection and import it into Postman.</p>
        <DownloadButton
          content={collection}
          filename="concerto-registration.postman_collection.json"
          label="Download Postman Collection"
        />
      </div>

      <div className="warn">
        <span>⚠️</span>
        <div>
          <strong>Security warning:</strong> Do not commit or share your Postman environment file if
          it contains a real access token. Use Postman environment variables and keep token values local.
        </div>
      </div>

      <div className="card no-hover">
        <h3 style={{ marginTop: 0 }}>Step-by-Step Walkthrough</h3>
        <ol>
          <li>
            <strong>Obtain an access token</strong> — use your organization's approved Docusign OAuth
            process to get a valid access token. Do not paste the token into this website.
          </li>
          <li>
            <strong>Open Postman</strong> and create a new request (or import the collection above).
          </li>
          <li>
            <strong>Set the method to POST</strong>.
          </li>
          <li>
            <strong>Set the URL:</strong>
            <CodeBlock code={regUrl} />
          </li>
          <li>
            <strong>Add headers:</strong>
            <CodeBlock code={`Authorization: Bearer <ACCESS_TOKEN>\nAccept: application/json\nContent-Type: application/json`} />
          </li>
          <li>
            <strong>Select Body → raw → JSON</strong>.
          </li>
          <li>
            <strong>Paste the model JSON:</strong>
            <CodeBlock code={modelJson} />
          </li>
          <li>
            <strong>Send the request</strong>.
          </li>
          <li>
            <strong>Review the response</strong> — a successful registration returns a <code>2xx</code> status.
          </li>
          <li>
            <strong>Verify in Maestro</strong> — confirm the model is available in the "Send Data to CLM"
            configuration (covered in the Verify step).
          </li>
        </ol>
      </div>

      <StepNav currentStep="register-postman" onNavigate={onNavigate} />
    </div>
  )
}
