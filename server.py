from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages = []  # Store messages in memory

@app.route("/")
def home():
    return "✅ Chat server is running!"

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

@app.route("/messages", methods=["POST"])
def post_message():
    data = request.get_json()
    if "user" in data and "text" in data:
        messages.append(data)
        return jsonify({"status": "ok"})
    return jsonify({"status": "error"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
