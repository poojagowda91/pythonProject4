import requests

base_uri = "https://rahulshettyacademy.com"
resource = "/maps/api/place/update/json"

url = base_uri + resource

query_parameter = {'qaclick123': '4632cff7ca3f4f35ff3c58ac495b32ee'}

request_body = {
    "place_id": "4632cff7ca3f4f35ff3c58ac495b32ee",
    "address": "123 walkaway,USA",
    "key": "qaclick123"
}

response = requests.put(url, params=query_parameter, json=request_body)

if response.status_code == 200:
    print("Successfull")
    print(response.json())
else:
    print("Not Successfull")
