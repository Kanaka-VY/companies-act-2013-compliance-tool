# Tool-119 — AI Service Summary Card

## Tech Stack
- Language: Python 3.11
- Framework: Flask 3.x (port 5000)
- AI Model: LLaMA-3.3-70b via Groq API
- Cache: Redis (15-min TTL, SHA256 key)
- Security: flask-limiter (30 req/min), input sanitisation

## 3 AI Endpoints
| Endpoint          | Method | Input         | Output                    |
|-------------------|--------|---------------|---------------------------|
| /describe         | POST   | issue text    | JSON: violation, section, severity |
| /recommend        | POST   | issue text    | JSON array: 3 actions     |
| /generate-report  | POST   | context text  | JSON: title, summary, key items |

## Security Measures
- Prompt injection detection (returns 400)
- Rate limiting: 30 requests/min per IP
- HTML stripping on all inputs
- PII audit: no personal data sent to Groq
- OWASP ZAP: 0 Critical, 0 High findings
- Fallback on Groq failure: {is_fallback: true}

## GitHub: [your repo URL here]
## Health check: http://localhost:5000/health