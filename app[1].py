from flask import Flask, render_template, request, jsonify
from urllib.parse import urlparse
import re
import os

app = Flask(__name__)

SUSPICIOUS_WORDS = {
    "verify", "login", "secure", "account", "update", "banking",
    "password", "wallet", "urgent", "gift", "free", "confirm"
}
SHORTENERS = {"bit.ly", "tinyurl.com", "t.co", "is.gd", "cutt.ly", "rb.gy"}

def analyze_url(raw_url):
    """Explainable starter checks only; not a guarantee that a URL is safe."""
    value = (raw_url or "").strip()
    if not value:
        return {"ok": False, "error": "Please enter a URL to analyze."}

    if not re.match(r"^https?://", value, re.I):
        value = "https://" + value

    try:
        parsed = urlparse(value)
        host = (parsed.hostname or "").lower().strip(".")
        if not host or "." not in host:
            return {"ok": False, "error": "Enter a valid domain, such as example.com."}
    except Exception:
        return {"ok": False, "error": "The URL could not be parsed. Please check it and try again."}

    reasons = []
    score = 0

    if parsed.scheme.lower() != "https":
        score += 15
        reasons.append("The URL does not use HTTPS.")

    if "@" in parsed.netloc:
        score += 20
        reasons.append("The URL contains an @ symbol in its address.")

    if len(value) > 100:
        score += 10
        reasons.append("The URL is unusually long.")

    if re.search(r"https?://\d{1,3}(?:\.\d{1,3}){3}", value, re.I):
        score += 25
        reasons.append("The URL uses an IP address instead of a typical domain name.")

    if host in SHORTENERS:
        score += 20
        reasons.append("The domain is a URL-shortening service, so the final destination is hidden.")

    labels = host.split(".")
    if len(labels) >= 5:
        score += 10
        reasons.append("The domain has many subdomain levels.")

    found_words = sorted({word for word in SUSPICIOUS_WORDS if word in value.lower()})
    if found_words:
        score += min(25, 5 * len(found_words))
        reasons.append("The URL contains words often used in social-engineering lures: " + ", ".join(found_words) + ".")

    if "-" in labels[0] and len(labels[0]) > 12:
        score += 5
        reasons.append("The first domain label is long and contains a hyphen.")

    score = min(score, 100)
    if score >= 60:
        level, label = "high", "High risk indicators"
    elif score >= 30:
        level, label = "medium", "Some suspicious indicators"
    else:
        level, label = "low", "Few indicators found"

    if not reasons:
        reasons.append("These basic checks did not find common URL warning signs. This does not prove the website is safe.")

    return {
        "ok": True,
        "url": value,
        "domain": host,
        "score": score,
        "level": level,
        "label": label,
        "reasons": reasons,
        "note": "Prototype analysis using explainable URL heuristics. No live threat-intelligence lookup is performed."
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/api/scan-url")
def scan_url():
    data = request.get_json(silent=True) or {}
    return jsonify(analyze_url(data.get("url", "")))

@app.post("/api/scan-text")
def scan_text():
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    if not text:
        return jsonify({"ok": False, "error": "Paste an SMS or email message first."}), 400

    lower = text.lower()
    patterns = {
        "Urgency or pressure": ["urgent", "immediately", "act now", "suspended", "within 24 hours"],
        "Credential request": ["password", "otp", "one-time password", "pin", "login"],
        "Money or reward lure": ["won", "prize", "free gift", "refund", "claim now"],
        "Suspicious link language": ["click here", "verify your account", "update your account", "bit.ly", "tinyurl"]
    }
    findings = []
    score = 0
    for title, terms in patterns.items():
        matches = [term for term in terms if term in lower]
        if matches:
            findings.append({"title": title, "matches": matches})
            score += min(25, 10 + 5 * (len(matches) - 1))

    score = min(score, 100)
    level = "high" if score >= 60 else "medium" if score >= 30 else "low"
    if not findings:
        findings.append({"title": "No common keyword patterns found", "matches": []})
    return jsonify({
        "ok": True, "score": score, "level": level, "findings": findings,
        "note": "Keyword-based prototype only. It may miss scams or flag legitimate messages; do not share OTPs or passwords."
    })

if __name__ == "__main__":
    # Safe local default; production hosting uses its own WSGI server.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=False)
