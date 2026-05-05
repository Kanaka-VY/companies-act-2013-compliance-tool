from flask import Blueprint, request, jsonify
import json

from services.groq_client import GroqClient

recommend_bp = Blueprint("recommend", __name__)


@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    if not data or "input" not in data:
        return jsonify({"error": "Input is required"}), 400

    user_input = data["input"]

    prompt = f"""
You are a compliance expert.

Based on the issue:
{user_input}

Provide EXACTLY 3 recommendations in VALID JSON format like:
[
  {{
    "action_type": "string",
    "description": "string",
    "priority": "High/Medium/Low"
  }}
]

IMPORTANT:
- Output ONLY JSON
- Do NOT add explanation
- Do NOT add text before/after JSON
"""

    response = GroqClient().call(prompt)
    output = response.get("content")

    try:
        parsed = json.loads(output)
    except (TypeError, json.JSONDecodeError):
        parsed = output

    return jsonify({
        "recommendations": parsed,
        "is_fallback": response.get("is_fallback", False)
    })
