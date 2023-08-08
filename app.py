from flask import Flask, request, render_template_string
from g4f.Provider import GetGpt
import g4f
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template_string(
        "<a href='https://github.com/Dqrshan/gpt-4'>Source</a>"
    )


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)
    response = g4f.ChatCompletion.create(
        messages=data["messages"], provider=GetGpt, model=g4f.models.gpt_35_turbo
    )
    return json.dumps({"response": response})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
