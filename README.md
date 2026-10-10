# AI-CyberShield
# 🛡️ AI CyberShield – Phishing & Scam Detection System

## 📌 About the Project

**AI CyberShield** is a web-based cybersecurity prototype designed to help users identify suspicious URLs and scam messages. It analyzes submitted inputs using predefined rules and patterns, then provides risk indications and basic safety guidance.

The goal is to improve cybersecurity awareness and help users recognize possible phishing attempts before interacting with suspicious content.

## 🎯 Objectives

- Identify suspicious patterns in URLs and messages.
- Display understandable risk indications.
- Provide basic safety recommendations.
- Promote awareness of phishing attacks and online scams.

## ✨ Features

- Simple and user-friendly web interface.
- Basic URL and message screening, depending on implemented functionality.
- Suspicious-pattern detection.
- Risk indications and safety guidance.
- Web-based application.

## 🛠️ Technologies Used

- **Python** – Backend programming
- **Flask** – Web framework
- **HTML** – Webpage structure
- **CSS** – User interface styling
- **JavaScript** – Frontend interactions
- **Gunicorn** – Production application server
- **Render** – Web hosting and deployment

## ⚙️ How It Works

1. The user enters a URL or suspicious message.
2. The application receives the submitted input.
3. The backend checks it against predefined rules and patterns.
4. The application generates a risk indication.
5. The result and relevant safety guidance are displayed.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/rajuvardhan847-afk/AI-CyberShield.git
```

### 2. Open the project directory

```bash
cd AI-CyberShield
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

### 5. Open in your browser

Visit:

```text
http://127.0.0.1:5000
```

## 🌐 Deployment

The application can be deployed using [Render](https://render.com/).

Typical deployment settings:

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

Ensure that `app.py`, `requirements.txt`, and the required frontend folders are located in the configured project root.

## 🔮 Future Enhancements

- Integrate a machine-learning classification model.
- Connect trusted threat-intelligence services.
- Add domain reputation checks.
- Improve detection using tested datasets.
- Develop a browser extension.
- Evaluate detection performance using accuracy, precision, recall, and F1-score.

## ⚠️ Limitations

This version is a prototype that uses predefined rules and patterns. It does not currently guarantee accurate detection of every scam, use a trained AI model, or provide live threat intelligence unless those capabilities are separately implemented.

**Always verify suspicious links through trusted sources. Never enter passwords or financial details on untrusted websites.**

## 👨‍💻 Author

**Rajavardhan P**

GitHub: [@rajuvardhan847-afk](https://github.com/rajuvardhan847-afk)

## 📄 License

This project is intended for educational and demonstration purposes. Add a license file if you want to specify the terms under which others may use or modify the project.
