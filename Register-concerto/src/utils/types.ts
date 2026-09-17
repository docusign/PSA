export type Environment = 'demo' | 'stage' | 'production' | 'custom'

export interface UserConfig {
  environment: Environment
  accountId: string
  namespace: string
  version: string
  customBaseUrl: string
  ctoModel: string
}

export const ENVIRONMENT_URLS: Record<Exclude<Environment, 'custom'>, string> = {
  demo: 'https://demo.services.docusign.net',
  stage: 'https://stage.services.docusign.net',
  production: 'https://services.docusign.net',
}

export const ENVIRONMENT_LABELS: Record<Environment, string> = {
  demo: 'Demo',
  stage: 'Stage',
  production: 'Production',
  custom: 'Custom',
}

export const STEPS = [
  { id: 'overview', label: 'Overview' },
  { id: 'prerequisites', label: 'Prerequisites' },
  { id: 'create-model', label: 'Create a Concerto Model' },
  { id: 'convert-model', label: 'Convert to JSON' },
  { id: 'register-postman', label: 'Register via Postman' },
  { id: 'register-curl', label: 'Register via cURL' },
  { id: 'register-vscode', label: 'Register via VS Code' },
  { id: 'verify', label: 'Verify in Maestro' },
  { id: 'troubleshooting', label: 'Troubleshooting' },
] as const

export type StepId = (typeof STEPS)[number]['id']

export const DEFAULT_CTO = `namespace DataToCLM@1.0.0

concept DataToCLM {
  o String EnvelopeId
}`

export function getBaseUrl(config: UserConfig): string {
  if (config.environment === 'custom') return config.customBaseUrl || '<BASE_URL>'
  return ENVIRONMENT_URLS[config.environment]
}

export function getRegistrationUrl(config: UserConfig): string {
  const base = getBaseUrl(config)
  const acct = config.accountId || '<ACCOUNT_ID>'
  return `${base}/v1/accounts/${acct}/workflows/models`
}

export function buildModelJson(config: UserConfig): string {
  const ns = config.namespace || 'DataToCLM'
  const ver = config.version || '1.0.0'
  const payload = {
    payload: {
      '$class': 'concerto.metamodel@1.0.0.Model',
      decorators: [],
      namespace: `${ns}@${ver}`,
      imports: [],
      declarations: [
        {
          '$class': 'concerto.metamodel@1.0.0.ConceptDeclaration',
          name: ns,
          isAbstract: false,
          properties: [
            {
              '$class': 'concerto.metamodel@1.0.0.StringProperty',
              name: 'EnvelopeId',
              isArray: false,
              isOptional: false,
            },
          ],
        },
      ],
    },
  }
  return JSON.stringify(payload, null, 2)
}

export function buildCurlCommand(config: UserConfig): string {
  const url = getRegistrationUrl(config)
  return `curl --request POST \\
  --url "${url}" \\
  --header "Authorization: Bearer \${DOCUSIGN_ACCESS_TOKEN}" \\
  --header "Accept: application/json" \\
  --header "Content-Type: application/json" \\
  --data @model-registration.json`
}

export function buildPostmanCollection(config: UserConfig): string {
  const url = getRegistrationUrl(config)
  const collection = {
    info: {
      name: 'Concerto Model Registration',
      schema: 'https://schema.getpostman.com/json/collection/v2.1.0/collection.json',
      description: 'Register a Concerto model with the Maestro API.',
    },
    variable: [
      { key: 'baseUrl', value: getBaseUrl(config), type: 'string' },
      { key: 'accountId', value: config.accountId || '{{accountId}}', type: 'string' },
      { key: 'accessToken', value: '{{accessToken}}', type: 'string' },
    ],
    item: [
      {
        name: 'Register Concerto Model',
        request: {
          method: 'POST',
          header: [
            { key: 'Authorization', value: 'Bearer {{accessToken}}', type: 'text' },
            { key: 'Accept', value: 'application/json', type: 'text' },
            { key: 'Content-Type', value: 'application/json', type: 'text' },
          ],
          body: {
            mode: 'raw',
            raw: buildModelJson(config),
            options: { raw: { language: 'json' } },
          },
          url: {
            raw: url,
            protocol: url.startsWith('https') ? 'https' : 'http',
            host: [getBaseUrl(config).replace(/^https?:\/\//, '')],
            path: ['v1', 'accounts', config.accountId || '{{accountId}}', 'workflows', 'models'],
          },
        },
        event: [
          {
            listen: 'test',
            script: {
              exec: [
                'pm.test("Status is 2xx", function () {',
                '    pm.response.to.be.success;',
                '});',
                'pm.test("Response has model info", function () {',
                '    var jsonData = pm.response.json();',
                '    pm.expect(jsonData).to.be.an("object");',
                '});',
              ],
              type: 'text/javascript',
            },
          },
        ],
      },
    ],
  }
  return JSON.stringify(collection, null, 2)
}

export function redactToken(text: string): string {
  return text.replace(/(Bearer\s+)[^\s"]+/gi, '$1<REDACTED>')
}
