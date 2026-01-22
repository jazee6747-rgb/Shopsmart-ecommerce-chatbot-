from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message", "").lower()

    if "hi" in msg or "hello" in msg:
        return jsonify({"reply": "Hello! How can I help you with shopping?"})

    if "product" in msg or "price" in msg:
        return jsonify({"reply": "We have mobiles, laptops, and accessories."})

    if "return" in msg:
        return jsonify({"reply": "We offer a 7-day return policy."})

    return jsonify({"reply": "I only answer shopping-related questions."})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=10000)
