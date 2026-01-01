import os
import requests

TELEGRAM_TOKEN = os.environ["7949377715:AAGjR4mAHxuObuDqIYaWz3G1GGVdhXf9hM8"]
TELEGRAM_CHAT_ID = os.environ["1087249095"]

def notify(item):
    msg = f"""🚨 INTERPELLO A045

{item['title']}

🔗 {item['url']}
"""
    url = f"https://api.telegram.org/bot{7949377715:AAGjR4mAHxuObuDqIYaWz3G1GGVdhXf9hM8}/sendMessage"
    requests.post(url, json={
        "chat_id": 1087249095,
        "text": msg
    })
