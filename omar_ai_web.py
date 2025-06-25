from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)
chatbot = pipeline("text-generation", model="gpt2")

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input:
            result = chatbot(user_input, max_length=100, do_sample=True)[0]["generated_text"]
            response = result.strip().replace("\n", " ")
    return render_template("index.html", response=response)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
