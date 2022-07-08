import json

import requests

url = "http://127.0.0.1:5000/echo"
# url = "" # For Negative Testing
data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.json())
