import requests

TOKEN = "ضع_التوكن_هنا"
CHAT_ID = "7498031156"

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def check():
    send_msg("📡 البوت يعمل الآن")

check()
