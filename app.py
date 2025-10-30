# Royal Gateway v1.0
# 👑 Created by Mohammad Ammarloo

from flask import Flask, request, jsonify
import os

# ساخت اپ Flask
app = Flask(name)

# روت تست پایه برای اطمینان از اجرا
@app.route("/")
def home():
    return "👑 Royal Gateway v1.0 is running successfully!"

# روت اصلی برای ارتباط با هسته رویال (نمونه ساده)
@app.route("/chat", methods=["POST"])
def chat_gateway():
    data = request.get_json(force=True)
    message = data.get("message", "")
    # پاسخ آزمایشی:
    response = f"Royal Gateway received: {message}"
    return jsonify({"response": response})

# اجرای مستقیم در حالت محلی (برای Render و Railway)
if name == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
