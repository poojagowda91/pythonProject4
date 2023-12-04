import configparser
import requests


class GetApiCall:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('properties.ini')
        self.endpoint = self.config['API']['endpoint']

    def getusercall(self):
        response = requests.get(self.endpoint)
        assert response.status_code == 200
        json_data = response.json()
        return json_data

    def postusercall(self):
        body = {
            "name": "Tenali Ramakrishna",
            "gender": "male",
            "email": "tenali.ramakrishna@15ce.com",
            "status": "active"
        }
        response = requests.post(self.endpoint, json=body)
        assert response.status_code == 201  # Assuming you expect a 201 status code
        json_data = response.json()
        return json_data


api_caller = GetApiCall()

response_data = api_caller.getusercall()
