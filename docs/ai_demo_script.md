# AI Demo Script — AI Developer 2

## My segment: Tech stack + Security (approx 60-90 seconds)

### Opening line (say exactly this):
"Our AI service is a Python Flask microservice running on port 5000,
powered by Groq's LLaMA-3.3-70b model via their free API."

### Live demo inputs (use these exact inputs — tested and confirmed working):

/describe input:
  "The company failed to hold its Annual General Meeting for FY 2023-24
   as required under Section 96 of the Companies Act 2013."

/recommend input:
  "Company has not filed its Annual Return MGT-7 for two consecutive years."

/generate-report input:
  "Conduct a full compliance review for a private limited company
   that has missed AGM, not filed AOC-4, and has a director without DIN."

### Expected outputs: [paste actual outputs from testing here]

### Security demo (60 seconds):
1. Open Postman
2. Call GET /api/compliance without JWT header
3. Show 401 Unauthorized response — say "No token, no access"
4. Call POST /describe with "Ignore previous instructions"
5. Show 400 response — say "Prompt injection blocked at middleware level"
6. Hold up SECURITY.md — "All threats documented, tested, and fixed"

### 60-second plain English explanation:
"We send the user's compliance data to Groq's LLaMA model in a carefully
structured prompt. The model responds with structured JSON — a violation
description, the exact section of the Companies Act, severity, and
recommended actions. If Groq is unavailable, we return a fallback response
so the app never crashes."

### Q&A answers (memorise these):
Q: What AI model?     A: LLaMA-3.3-70b via Groq API, free tier
Q: What if AI fails?  A: Returns fallback JSON with is_fallback: true
Q: How is it secured? A: Rate limiting, injection detection, JWT, PII audit