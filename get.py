import requests
import json

data = requests.get('http://127.0.0.1:5000/', headers = {'token':'my'})

print(data.json())