import { useState, useCallback } from 'react'

interface Props {
  code: string
  variant?: 'default' | 'prompt'
  label?: string
}

export function CodeBlock({ code, variant = 'default', label }: Props) {
  const [copied, setCopied] = useState(false)

  const handleCopy = useCallback(() => {
    navigator.clipboard.writeText(code).then(() => {
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    })
  }, [code])

  return (
    <div>
      {label && <div className="lbl">{label}</div>}
      <div className={`block ${variant === 'prompt' ? 'prompt' : ''}`}>
        <button
          className={`copy-btn ${copied ? 'copied' : ''}`}
          onClick={handleCopy}
          aria-label="Copy to clipboard"
        >
          {copied ? '✓ Copied' : 'Copy'}
        </button>
        {code}
      </div>
    </div>
  )
}
