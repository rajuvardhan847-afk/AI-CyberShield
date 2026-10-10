# AI CyberShield

A Flask-based educational prototype that checks URL patterns and SMS/email text for common scam indicators.

## Important limitations
- This is a rule-based prototype, not a trained AI model.
- It does not query live threat-intelligence databases or open/check the destination website.
- A low score does **not** mean a URL or message is safe. A high score is not proof of a scam.
- Do not paste passwords, OTPs, private messages, or other sensitive information.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Run `python -m pip install -r requirements.txt`.
4. Run `python app.py`.
5. Open `http://127.0.0.1:5000`.

## Deploy on Render
1. Push the *extracted project files and folders* to a GitHub repository (not only this ZIP file).
2. In Render, create a new Web Service and connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Deploy. The included `render.yaml` also records these settings.

No API keys or secrets are required for this prototype.
