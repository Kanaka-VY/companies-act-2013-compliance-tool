from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import re, html

from routes.describe import describe_bp
from routes.health import health_bp
from routes.recommend import recommend_bp
from routes.report import report_bp

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"forget your prompt",
    r"you are now",
    r"system:",
]

def sanitise_input(text: str) -> str:
    text = html.escape(text.strip())
    if not text:
        return None
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return None
    return text

@app.before_request
def validate_input():
    if request.method == "POST" and request.is_json:
        data = request.get_json()
        for key, value in data.items():
            if isinstance(value, str):
                clean = sanitise_input(value)
                if clean is None:
                    return jsonify({
                        "error": "Invalid input detected",
                        "code": "INJECTION_DETECTED"
                    }), 400


app.register_blueprint(health_bp)
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(report_bp)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
