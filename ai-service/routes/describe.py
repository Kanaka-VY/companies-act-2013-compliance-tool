from flask import Blueprint, request, jsonify
import json

from services.groq_client import GroqClient

describe_bp = Blueprint("describe", __name__)


@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    if not data or "input" not in data:
        return jsonify({"error": "Input is required"}), 400

    user_input = data["input"]

    prompt = f"""
You are a compliance AI assistant.

Given the company data:
{user_input}

Generate:
- Summary
- Risk Level (Low/Medium/High)
- Key Issues
- Suggestions
"""

    response = GroqClient().call(prompt)
    output = response.get("content")

    try:
        parsed = json.loads(output)
        if isinstance(parsed, dict):
            parsed["is_fallback"] = response.get("is_fallback", False)
            return jsonify(parsed)
    except (TypeError, json.JSONDecodeError):
        pass

    return jsonify({
        "content": output,
        "is_fallback": response.get("is_fallback", False),
        "generated_at": "now"
    })
