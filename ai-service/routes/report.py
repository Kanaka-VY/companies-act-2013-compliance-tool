from flask import Blueprint, request, jsonify
import json

from services.groq_client import GroqClient

report_bp = Blueprint("report", __name__)


@report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()

    if not data or "input" not in data:
        return jsonify({"error": "Input is required"}), 400

    user_input = data["input"]

    prompt = f"""
You are a compliance AI assistant.

Given the issue:
{user_input}

Generate a structured JSON report:

{{
  "title": "string",
  "summary": "string",
  "overview": "string",
  "key_items": ["item1", "item2"],
  "recommendations": ["rec1", "rec2"]
}}

IMPORTANT:
- Output ONLY JSON
- No extra text
"""

    response = GroqClient().call(prompt)
    output = response.get("content")

    try:
        parsed = json.loads(output)
        if isinstance(parsed, dict):
            parsed["is_fallback"] = response.get("is_fallback", False)
        return jsonify(parsed)
    except (TypeError, json.JSONDecodeError):
        return jsonify({
            "content": output,
            "is_fallback": response.get("is_fallback", False)
        })
