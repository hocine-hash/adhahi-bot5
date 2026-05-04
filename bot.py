import os
import requests

URL = "https://adhahi.dz"

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def check():
    try:
        send_msg("✅ البوت يعمل بشكل صحيح")  # اختبار

        r = requests.get(URL, timeout=10)

        if "سوق أهراس" in r.text and "غير متوفر" not in r.text:
            send_msg("🚨 الحجز فتح في سوق أهراس!\nhttps://adhahi.dz")

    except Exception as e:
        print(e)

check()
