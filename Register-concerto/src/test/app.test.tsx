import { describe, it, expect, vi } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import App from '../App'

describe('App', () => {
  it('renders the header', () => {
    render(<App />)
    expect(screen.getByText('Concerto Model Registration')).toBeInTheDocument()
  })

  it('shows the overview hero on initial load', () => {
    render(<App />)
    expect(screen.getByText('Concerto Model Registration Guide')).toBeInTheDocument()
  })

  it('navigates to prerequisites when clicking next', () => {
    render(<App />)
    fireEvent.click(screen.getByText('Prerequisites →'))
    expect(screen.getByText('Configure Your Environment')).toBeInTheDocument()
  })

  it('shows environment selector in prerequisites', () => {
    render(<App />)
    fireEvent.click(screen.getByText('Prerequisites →'))
    expect(screen.getByText('Demo')).toBeInTheDocument()
    expect(screen.getByText('Stage')).toBeInTheDocument()
    expect(screen.getByText('Production')).toBeInTheDocument()
    expect(screen.getByText('Custom')).toBeInTheDocument()
  })

  it('does not make any API calls', () => {
    const fetchSpy = vi.spyOn(globalThis, 'fetch')
    const xhrSpy = vi.spyOn(XMLHttpRequest.prototype, 'open')
    render(<App />)
    expect(fetchSpy).not.toHaveBeenCalled()
    expect(xhrSpy).not.toHaveBeenCalled()
    fetchSpy.mockRestore()
    xhrSpy.mockRestore()
  })

  it('does not render any password or token input fields', () => {
    render(<App />)
    const inputs = document.querySelectorAll('input')
    inputs.forEach(input => {
      expect(input.type).not.toBe('password')
      expect(input.name).not.toMatch(/token|secret|password|key/i)
    })
  })

  it('shows account ID disclaimer', () => {
    render(<App />)
    fireEvent.click(screen.getByText('Prerequisites →'))
    expect(screen.getByText(/Account ID identifies the target account/)).toBeInTheDocument()
  })

  it('navigates through sidebar steps', () => {
    render(<App />)
    fireEvent.click(screen.getByText('Troubleshooting'))
    expect(screen.getByText(/Common errors you may encounter/)).toBeInTheDocument()
  })
})
