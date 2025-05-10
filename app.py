from flask import Flask, request
import os

app = Flask(__name__)

VK_CONFIRMATION_TOKEN = os.getenv("VK_CONFIRMATION_TOKEN")
VK_SECRET = os.getenv("VK_SECRET")

@app.route("/", methods=["POST"])
def vk_webhook():
    data = request.json

    if data["type"] == "confirmation":
        return VK_CONFIRMATION_TOKEN

    elif data["type"] == "message_new":
        message = data["object"]["message"]["text"]
        user_id = data["object"]["message"]["from_id"]
        # здесь можно подключить ChatGPT или логику поиска
        print(f"Новое сообщение от {user_id}: {message}")
        return "ok"

    return "ok"

@app.route("/", methods=["GET"])
def health_check():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
