
# OmarAI Web Chatbot
# Developed by Omar Ciriaco

from flask import Flask, request, render_template_string
from transformers import pipeline

app = Flask(__name__)
chatbot = pipeline("text-generation", model="gpt2")

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>OmarAI - Developed by Omar Ciriaco</title>
</head>
<body>
    <h1>🤖 Welcome to OmarAI</h1>
    <h3>Where your thoughts aren’t your limitations</h3>
    <p><em>Developed by Omar Ciriaco</em></p>
    <form method="post">
        <label for="user_input">You:</label><br>
        <input type="text" id="user_input" name="user_input" style="width: 400px;"><br><br>
        <input type="submit" value="Send">
    </form>
    {% if response %}
        <p><strong>OmarAI:</strong> {{ response }}</p>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input:
            result = chatbot(user_input, max_length=50, do_sample=True, top_k=50)[0]['generated_text']
            response = result.strip().replace("\n", " ")
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)
