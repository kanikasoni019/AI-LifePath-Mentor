from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from ai_engine import generate_reply
import os

app = Flask(__name__, static_folder='../frontend', template_folder='../frontend')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/chat')
def chat_page():
    return send_from_directory('../frontend', 'chat.html')

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.get_json() or {}
    user_input = data.get("message", "")
    reply, emotion, confidence = generate_reply(user_input)
    return jsonify({"reply": reply, "emotion": emotion, "confidence": confidence})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)