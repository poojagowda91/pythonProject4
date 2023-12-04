import requests


def send_test_result(test_name, status):
    test_result = {"test_name": test_name, "status": status}
    dashboard_url = 'http://localhost:8000/api/test_results'

    try:
        response = requests.post(dashboard_url, json=test_result)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send test result to the dashboard: {str(e)}")
