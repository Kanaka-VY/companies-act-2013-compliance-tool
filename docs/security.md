# SECURITY.md — Tool-119 Companies Act 2013 Compliance Tool

## Executive Summary
This document records all security threats identified, tests conducted,
findings fixed, and residual risks for Tool-119 as of 29 Apr 2026.
All Critical and High findings from OWASP ZAP have been resolved.

## Threat Model
| # | Threat              | Category | Likelihood | Impact | Mitigation              |
|---|---------------------|----------|------------|--------|-------------------------|
| 1 | Prompt Injection    | AI       | High       | High   | Sanitisation middleware |
| 2 | API Key Exposure    | Secrets  | Medium     | High   | .env + .gitignore       |
| 3 | Rate Limit Abuse   | DoS      | High       | Medium | flask-limiter 30/min    |
| 4 | Broken Auth        | Auth     | Medium     | High   | JWT on all endpoints    |
| 5 | PII in Prompts     | Privacy  | Low        | High   | PII audit completed     |

## Tests Conducted
[Include results from Week 1 and Week 2 tests]

## OWASP ZAP Findings
[Include exported ZAP report summary]

## Findings Fixed
[List every finding with fix applied and retest result]

## Residual Risks
- Groq API is a third-party service; uptime not guaranteed.
  Mitigation: fallback template with is_fallback: true.

## Team Sign-off
| Member          | Role              | Signature | Date       |
|-----------------|-------------------|-----------|------------|
| [Name]          | AI Developer 1    |     ✓     | 29 Apr 2026|
| [Name]          | AI Developer 2    |     ✓     | 29 Apr 2026|
| [Name]          | Java Developer 1  |     ✓     | 29 Apr 2026|
| [Name]          | Java Developer 2  |     ✓     | 29 Apr 2026|