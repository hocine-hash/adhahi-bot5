import requests

URL = "https://adhahi.dz"

TOKEN = "8530154647:AAESvKZjbvg_zU6FMZ8DIROkIMCv-8KdwEQ"
CHAT_ID = "-1003836797030"

def send_msg(text):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    except Exception as e:
        print("error:", e)

def check():
    try:
        r = requests.get(URL, timeout=10)

        print("site checked")

        if "سوق أهراس" in r.text and "غير متوفر" not in r.text:
            send_msg("🚨 الحجز فتح في سوق أهراس")
    except Exception as e:
        print("site error:", e)

check()
