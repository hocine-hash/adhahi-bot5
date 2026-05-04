import requests

URL = "https://adhahi.dz"

TOKEN = "8530154647:AAESvKZjbvg_zU6FMZ8DIROkIMCv-8KdwEQ"
CHAT_ID = "7498031156"

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def check():
    r = requests.get(URL, timeout=10)

    # شرط سوق أهراس
    if "سوق أهراس" in r.text and "غير متوفر" not in r.text:
        send_msg("🚨 الحجز فتح في سوق أهراس!\nhttps://adhahi.dz")

check()
