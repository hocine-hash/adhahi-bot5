import requests
import os

URL = "https://adhahi.dz"

TOKEN = "8530154647:AAESvKZjbvg_zU6FMZ8DIROkIMCv-8KdwEQ"
CHAT_ID = "-1003836797030"

STATE_FILE = "state.txt"


def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )


def get_state():
    return open(STATE_FILE).read().strip() if os.path.exists(STATE_FILE) else ""


def save_state(s):
    open(STATE_FILE, "w").write(s)


def check():
    r = requests.get(URL, timeout=10)
    text = r.text

    if "سوق أهراس" in text:
        status = "open" if "غير متوفر" not in text else "closed"
    else:
        status = "unknown"

    if status != get_state() and status != "unknown":
        send("🚨 الحجز فتح في سوق أهراس" if status == "open" else "❌ الحجز مغلق")
        save_state(status)


check()
