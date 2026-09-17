import { useState, useCallback } from 'react'
import { STEPS, type StepId, type UserConfig } from './utils/types'
import { Overview } from './steps/Overview'
import { Prerequisites } from './steps/Prerequisites'
import { CreateModel } from './steps/CreateModel'
import { ConvertModel } from './steps/ConvertModel'
import { RegisterPostman } from './steps/RegisterPostman'
import { RegisterCurl } from './steps/RegisterCurl'
import { RegisterVSCode } from './steps/RegisterVSCode'
import { Verify } from './steps/Verify'
import { Troubleshooting } from './steps/Troubleshooting'

const DEFAULT_CONFIG: UserConfig = {
  environment: 'demo',
  accountId: '',
  namespace: 'DataToCLM',
  version: '1.0.0',
  customBaseUrl: '',
  ctoModel: '',
}

export default function App() {
  const [currentStep, setCurrentStep] = useState<StepId>('overview')
  const [config, setConfig] = useState<UserConfig>(DEFAULT_CONFIG)
  const [visitedSteps, setVisitedSteps] = useState<Set<StepId>>(new Set(['overview']))

  const handleNavigate = useCallback((step: StepId) => {
    setCurrentStep(step)
    setVisitedSteps(prev => new Set(prev).add(step))
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }, [])

  const handleConfigChange = useCallback((updates: Partial<UserConfig>) => {
    setConfig(prev => ({ ...prev, ...updates }))
  }, [])

  const currentIdx = STEPS.findIndex(s => s.id === currentStep)

  function renderStep() {
    switch (currentStep) {
      case 'overview':
        return <Overview config={config} onNavigate={handleNavigate} />
      case 'prerequisites':
        return <Prerequisites config={config} onChange={handleConfigChange} onNavigate={handleNavigate} />
      case 'create-model':
        return <CreateModel config={config} onChange={handleConfigChange} onNavigate={handleNavigate} />
      case 'convert-model':
        return <ConvertModel config={config} onNavigate={handleNavigate} />
      case 'register-postman':
        return <RegisterPostman config={config} onNavigate={handleNavigate} />
      case 'register-curl':
        return <RegisterCurl config={config} onNavigate={handleNavigate} />
      case 'register-vscode':
        return <RegisterVSCode config={config} onNavigate={handleNavigate} />
      case 'verify':
        return <Verify onNavigate={handleNavigate} />
      case 'troubleshooting':
        return <Troubleshooting onNavigate={handleNavigate} />
    }
  }

  return (
    <>
      <div className="utility">
        <span>Docusign Platform — Instructional Guide Only</span>
      </div>

      <header className="top">
        <div className="top-title">
          <svg viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg" width="28" height="28">
            <rect width="36" height="36" rx="8" fill="#4C00FF"/>
            <path d="M10 18l5 5 11-11" stroke="#fff" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          Concerto Model Registration
        </div>
      </header>

      <div className="wrap">
        <aside className="aside" role="navigation" aria-label="Steps">
          <ul className="stepper">
            {STEPS.map((step, idx) => {
              const isActive = step.id === currentStep
              const isDone = visitedSteps.has(step.id) && idx < currentIdx
              return (
                <li
                  key={step.id}
                  className={`step ${isActive ? 'active' : ''} ${isDone ? 'done' : ''}`}
                  onClick={() => handleNavigate(step.id)}
                  role="button"
                  tabIndex={0}
                  aria-current={isActive ? 'step' : undefined}
                  onKeyDown={e => { if (e.key === 'Enter' || e.key === ' ') handleNavigate(step.id) }}
                >
                  <div className="ring">
                    <span className="ring-num">
                      {isDone ? '✓' : idx + 1}
                    </span>
                  </div>
                  <span className="step-label">{step.label}</span>
                </li>
              )
            })}
          </ul>
        </aside>

        <main className="main">
          {renderStep()}
        </main>
      </div>
    </>
  )
}
