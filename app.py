from flask import Flask, request
from g4f.Provider import DeepAi
import g4f
import json

app = Flask(__name__)


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=data["messages"],
        provider=DeepAi,
    )
    return json.dumps({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
