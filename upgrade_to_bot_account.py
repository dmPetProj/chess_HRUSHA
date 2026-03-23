import requests

api = "Bearer " + "сюда API ключ"   # <------------------------------
r = requests.post("https://lichess.org/api/bot/account/upgrade", headers = {"Authorization" : api})
print(r.status_code, r.text)
