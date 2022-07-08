# Client to test the Flask
import json

import requests

url = "http://127.0.0.1:5000/echo"
# url = "" # For Negative Testing
data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# r = requests.post(url, data=json.dumps(data), headers=headers)

# From requests 2.4.2 (https://pypi.python.org/pypi/requests), the "json" parameter is supported. No need to specify
# "Content-Type". So the shorter version:
r = requests.post(url, json={'test': 'cheers'})
print(r.json())



# https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests
