from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages = []  # store messages in memory for now

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    name = data.get("name", "Anon")
    text = data.get("text", "")
    messages.append(f"{name}: {text}")
    return jsonify({"status": "ok"})

@app.route("/recv", methods=["GET"])
def recv():
    return jsonify(messages[-50:])  # last 50 messages

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
