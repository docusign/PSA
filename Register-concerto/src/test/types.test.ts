import { describe, it, expect } from 'vitest'
import {
  getBaseUrl,
  getRegistrationUrl,
  buildModelJson,
  buildCurlCommand,
  buildPostmanCollection,
  redactToken,
  type UserConfig,
} from '../utils/types'

const baseConfig: UserConfig = {
  environment: 'demo',
  accountId: '12345678-abcd-efgh-ijkl-123456789012',
  namespace: 'DataToCLM',
  version: '1.0.0',
  customBaseUrl: '',
  ctoModel: '',
}

describe('getBaseUrl', () => {
  it('returns demo URL for demo environment', () => {
    expect(getBaseUrl(baseConfig)).toBe('https://demo.services.docusign.net')
  })

  it('returns stage URL for stage environment', () => {
    expect(getBaseUrl({ ...baseConfig, environment: 'stage' })).toBe('https://stage.services.docusign.net')
  })

  it('returns production URL for production environment', () => {
    expect(getBaseUrl({ ...baseConfig, environment: 'production' })).toBe('https://services.docusign.net')
  })

  it('returns custom URL for custom environment', () => {
    expect(getBaseUrl({ ...baseConfig, environment: 'custom', customBaseUrl: 'https://my.env.net' }))
      .toBe('https://my.env.net')
  })

  it('returns placeholder when custom URL is empty', () => {
    expect(getBaseUrl({ ...baseConfig, environment: 'custom', customBaseUrl: '' }))
      .toBe('<BASE_URL>')
  })
})

describe('getRegistrationUrl', () => {
  it('inserts account ID into URL', () => {
    const url = getRegistrationUrl(baseConfig)
    expect(url).toContain(baseConfig.accountId)
    expect(url).toBe('https://demo.services.docusign.net/v1/accounts/12345678-abcd-efgh-ijkl-123456789012/workflows/models')
  })

  it('uses placeholder when account ID is empty', () => {
    const url = getRegistrationUrl({ ...baseConfig, accountId: '' })
    expect(url).toContain('<ACCOUNT_ID>')
  })

  it('uses correct base URL per environment', () => {
    expect(getRegistrationUrl({ ...baseConfig, environment: 'production' }))
      .toContain('https://services.docusign.net')
    expect(getRegistrationUrl({ ...baseConfig, environment: 'stage' }))
      .toContain('https://stage.services.docusign.net')
  })
})

describe('buildModelJson', () => {
  it('produces valid JSON', () => {
    const json = buildModelJson(baseConfig)
    expect(() => JSON.parse(json)).not.toThrow()
  })

  it('includes namespace and version', () => {
    const parsed = JSON.parse(buildModelJson(baseConfig))
    expect(parsed.payload.namespace).toBe('DataToCLM@1.0.0')
  })

  it('uses custom namespace and version', () => {
    const parsed = JSON.parse(buildModelJson({ ...baseConfig, namespace: 'MyModel', version: '2.0.0' }))
    expect(parsed.payload.namespace).toBe('MyModel@2.0.0')
  })

  it('includes the concerto metamodel class', () => {
    const parsed = JSON.parse(buildModelJson(baseConfig))
    expect(parsed.payload['$class']).toBe('concerto.metamodel@1.0.0.Model')
  })

  it('includes declarations with properties', () => {
    const parsed = JSON.parse(buildModelJson(baseConfig))
    expect(parsed.payload.declarations).toHaveLength(1)
    expect(parsed.payload.declarations[0].properties).toHaveLength(1)
    expect(parsed.payload.declarations[0].properties[0].name).toBe('EnvelopeId')
  })
})

describe('buildCurlCommand', () => {
  it('includes the registration URL', () => {
    const cmd = buildCurlCommand(baseConfig)
    expect(cmd).toContain(baseConfig.accountId)
  })

  it('uses environment variable for token, not a hardcoded value', () => {
    const cmd = buildCurlCommand(baseConfig)
    expect(cmd).toContain('${DOCUSIGN_ACCESS_TOKEN}')
    expect(cmd).not.toMatch(/Bearer [A-Za-z0-9]/)
  })

  it('references model-registration.json file', () => {
    const cmd = buildCurlCommand(baseConfig)
    expect(cmd).toContain('@model-registration.json')
  })

  it('includes required headers', () => {
    const cmd = buildCurlCommand(baseConfig)
    expect(cmd).toContain('Content-Type: application/json')
    expect(cmd).toContain('Accept: application/json')
    expect(cmd).toContain('Authorization: Bearer')
  })
})

describe('buildPostmanCollection', () => {
  it('produces valid JSON', () => {
    const json = buildPostmanCollection(baseConfig)
    expect(() => JSON.parse(json)).not.toThrow()
  })

  it('contains placeholder variables', () => {
    const parsed = JSON.parse(buildPostmanCollection(baseConfig))
    const varKeys = parsed.variable.map((v: { key: string }) => v.key)
    expect(varKeys).toContain('baseUrl')
    expect(varKeys).toContain('accountId')
    expect(varKeys).toContain('accessToken')
  })

  it('uses {{accessToken}} placeholder, not a real token', () => {
    const json = buildPostmanCollection(baseConfig)
    expect(json).toContain('{{accessToken}}')
  })

  it('includes test script', () => {
    const parsed = JSON.parse(buildPostmanCollection(baseConfig))
    const events = parsed.item[0].event
    expect(events).toBeDefined()
    expect(events[0].listen).toBe('test')
  })
})

describe('redactToken', () => {
  it('redacts bearer tokens', () => {
    expect(redactToken('Bearer eyJhbGciOiJIUzI1NiJ9.abc')).toBe('Bearer <REDACTED>')
  })

  it('leaves text without tokens unchanged', () => {
    expect(redactToken('no token here')).toBe('no token here')
  })

  it('is case insensitive', () => {
    expect(redactToken('bearer mytoken123')).toBe('bearer <REDACTED>')
  })
})

describe('no token collection', () => {
  it('curl command never contains a hardcoded token value', () => {
    const cmd = buildCurlCommand(baseConfig)
    expect(cmd).not.toMatch(/Bearer [A-Za-z0-9+/=]{10,}/)
  })

  it('postman collection uses placeholder for token', () => {
    const json = buildPostmanCollection(baseConfig)
    const parsed = JSON.parse(json)
    const tokenVar = parsed.variable.find((v: { key: string }) => v.key === 'accessToken')
    expect(tokenVar.value).toBe('{{accessToken}}')
  })
})

describe('empty or invalid account IDs', () => {
  it('uses placeholder for empty account ID in URL', () => {
    const url = getRegistrationUrl({ ...baseConfig, accountId: '' })
    expect(url).toContain('<ACCOUNT_ID>')
    expect(url).not.toContain('/accounts//workflows')
  })

  it('uses the raw value for non-UUID account IDs', () => {
    const url = getRegistrationUrl({ ...baseConfig, accountId: 'not-a-uuid' })
    expect(url).toContain('not-a-uuid')
  })
})
