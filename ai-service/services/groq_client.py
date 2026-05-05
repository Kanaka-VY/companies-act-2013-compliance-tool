import os, time, logging
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class GroqClient:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=api_key) if api_key else None
        self.model = "llama-3.3-70b-versatile"

    def call(self, prompt: str, temperature: float = 0.3, max_tokens: int = 1000) -> dict:
        if self.client is None:
            return {
                "content": "AI service temporarily unavailable.",
                "is_fallback": True
            }

        for attempt in range(3):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                return {
                    "content": response.choices[0].message.content,
                    "is_fallback": False
                }
            except Exception as e:
                logger.error(f"Groq attempt {attempt+1} failed: {e}")
                if attempt < 2:
                    time.sleep(2 ** attempt)
        return {
            "content": "AI service temporarily unavailable.",
            "is_fallback": True
        }
