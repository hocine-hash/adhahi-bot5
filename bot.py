import requests
import os

URL = "https://adhahi.dz"

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def check():
    try:
        r = requests.get(URL, timeout=10)

        # شرط سوق أهراس
        if "سوق أهراس" in r.text and "غير متوفر" not in r.text:
            send_msg("🚨 الحجز فتح في سوق أهراس!\nhttps://adhahi.dz")
    except:
        pass

check()
