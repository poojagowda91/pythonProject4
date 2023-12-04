import requests

# Define the base URL and resource path
base_url = "https://rahulshettyacademy.com"
resource = "/maps/api/place/add/json"

# Construct the full URL
url = base_url + resource

# Define the query parameter
query_params = {
    "key": "qaclick123"
}

# Define the request body
request_body = {
    "location": {
        "lat": -38.383494,
        "lng": 33.427362
    },
    "accuracy": 50,
    "name": "21 Fort Vale house",
    "phone_number": "(+91) 983 793 3937",
    "address": "31, side layout, cohen 09",
    "types": ["pickle park", "train"],
    "website": "http://google.com",
    "language": "English-IN"
}

# Make the POST request
response = requests.post(url, params=query_params, json=request_body)

# Check the response
if response.status_code == 200:
    print("POST request was successful.")
    print("Response:")
    print(response.json())
else:
    print(f"POST request failed with status code {response.status_code}")
    print("Response:")
    print(response.text)
