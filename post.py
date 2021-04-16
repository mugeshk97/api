import requests
import json

data = requests.post('http://127.0.0.1:5000/food', headers = {'token': 'my'}, json= {'name': 'Mugesh'})
print(data.json())