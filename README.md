# 🛡️ AI Bug Report Generator

An AI-powered tool that helps bug bounty hunters and security researchers generate professional, structured vulnerability reports using GPT.

---

## 🚀 Live Demo

👉 [Try it on Streamlit (if deployed)](https://yourusername-ai-bug-report-generator.streamlit.app)

---

## ✨ Features

- Select vulnerability type (IDOR, OAuth misconfig, 2FA bypass, etc.)
- Enter details like scope, steps to reproduce, impact, and optional fix
- Generates well-structured bug bounty report using GPT
- Markdown output for easy copy-paste into HackerOne or Bugcrowd
- Built with **Streamlit** and **OpenAI API**

---

## 🧠 How It Works

1. You provide details about a vulnerability.
2. The app sends that info to the OpenAI GPT API.
3. GPT returns a complete report formatted for bug bounty platforms.

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **OpenAI API (GPT-3.5-turbo / GPT-4)**
- **dotenv** (for managing API keys securely)

---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/alihassankhan76/ai-bug-report-generator.git
cd ai-bug-report-generator
pip install -r requirements.txt
