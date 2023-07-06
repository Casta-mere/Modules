import requests
import json

url = 'http://118.31.103.3:8888'
data = {'key1': 'value1', 'key2': 'value2'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.get(url, data=json.dumps(data), headers=headers)
print(r.text)