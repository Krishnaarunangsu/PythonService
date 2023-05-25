# Client to test the Flask
import json

import requests

# url = "http://127.0.0.1:5000/echo"
# url = "http://127.0.0.1:5000/create_record"
# url = "http://127.0.0.1:5000/update_record"
# url = "http://127.0.0.1:5000/get_records/Arunangsu"
# url = "http://127.0.0.1:5000/get_all_records"
url = "http://127.0.0.1:5000/delete_record"
# url = "" # For Negative Testing
# data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
# data = {'name': 'Ayan', 'email': 'ayan.bose@yahoo.com'}
data = {'name': 'Ayan'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# r = requests.post(url, data=json.dumps(data), headers=headers)
# r = requests.put(url, data=json.dumps(data), headers=headers)
# r = requests.get(url, headers=headers)
r = requests.delete(url, data=json.dumps(data), headers=headers)

# From requests 2.4.2 (https://pypi.python.org/pypi/requests), the "json" parameter is supported. No need to specify
# "Content-Type". So the shorter version:
# r = requests.post(url, json={'test': 'cheers'})
# print(r.json())
print(json.dumps(r.json(), indent=3))

# https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests
