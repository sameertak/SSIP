# from _datetime import datetime
# print(datetime.now())
import requests

header = {
'Authorization': 'Token 5e5a201fb2e4b04afb210825b1032135bf307063'
}

r = requests.get('http://127.0.0.1:8000/verify/time_based/9512519226/', headers=header)
print(r.text)