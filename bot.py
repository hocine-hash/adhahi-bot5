import requests

TOKEN = "حط_توكن_هنا"
CHAT_ID = "حط_الرقم_هنا"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url, data={"chat_id": CHAT_ID, "text": "اختبار فقط"})
