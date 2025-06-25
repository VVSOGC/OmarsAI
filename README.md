# OmarAI

**OmarAI** is a simple web-based AI chatbot powered by GPT-2 using Hugging Face Transformers.

> "Welcome to OmarAI — where your thoughts aren’t your limitations."

Developed by **Omar Ciriaco**.

## How to Run Locally

```bash
pip install -r requirements.txt
python omar_ai_web.py
```

## How to Deploy on Render

1. Create a free account at [render.com](https://render.com)
2. Create a new Web Service and connect your GitHub repo
3. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn omar_ai_web:app`
