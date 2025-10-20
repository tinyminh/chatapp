from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow Tkinter client to connect easily

# In-memory message store
messages = []

@app.route('/')
def home():
    return "Chat server is running!"

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    if not data or 'user' not in data or 'text' not in data:
        return jsonify({"error": "Invalid data"}), 400

    messages.append({
        "user": data['user'],
        "text": data['text']
    })
    print(f"Message received: {data}")
    return jsonify({"status": "ok"}), 200

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    # Render requires using PORT from environment variable
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
