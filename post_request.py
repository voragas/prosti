import requests
import json
r = requests.post('http://165.22.143.166/ping', data = {})
json_string = r.text
parsed_string = json.loads(json_string)
print(parsed_string)