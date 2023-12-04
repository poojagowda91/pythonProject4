import requests

base_uri = "https://rahulshettyacademy.com"
query_parameters = {'qaclick123': '4632cff7ca3f4f35ff3c58ac495b32ee'}
resource = "/maps/api/place/get/json"

url = base_uri + resource


def getgoogleapicall():
    try:
        response = requests.get(url, params=query_parameters)
        response.raise_for_status()  # Check for HTTP errors
        if response.status_code == 200:
            print("GET request was successful.")
            print("Response:")
            print(response.json())
        else:
            print(f"GET request failed with status code {response.status_code}")
            print("Response:")
            print(response.text)
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")


getgoogleapicall()
