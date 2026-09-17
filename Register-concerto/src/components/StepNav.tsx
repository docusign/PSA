import { STEPS, type StepId } from '../utils/types'

interface Props {
  currentStep: StepId
  onNavigate: (step: StepId) => void
}

export function StepNav({ currentStep, onNavigate }: Props) {
  const idx = STEPS.findIndex(s => s.id === currentStep)
  const prev = idx > 0 ? STEPS[idx - 1] : null
  const next = idx < STEPS.length - 1 ? STEPS[idx + 1] : null

  return (
    <div className="step-nav">
      {prev ? (
        <button className="btn btn-secondary" onClick={() => onNavigate(prev.id)}>
          ← {prev.label}
        </button>
      ) : <span />}
      {next ? (
        <button className="btn btn-primary" onClick={() => onNavigate(next.id)}>
          {next.label} →
        </button>
      ) : <span />}
    </div>
  )
}
