from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# Initialize an empty list for test results
test_results = []


@app.route('/')
def dashboard():
    return render_template('dashboard.html', test_results=test_results)


@app.route('/api/test_results', methods=['POST'])
def receive_test_result():
    try:
        data = request.get_json()
        print(f"Received test result: {data}")
        test_results.append(data)
        print(f"Updated test results: {test_results}")
        return jsonify({"message": "Test result received successfully"}), 201
    except Exception as e:
        print(f"Error processing test result: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Specify the port (e.g., 8000)
    app.run(debug=True, port=8000)
