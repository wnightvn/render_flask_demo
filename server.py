from flask import Flask, send_file, request, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": "admin",
    "user": "password123"
}

@app.before_request
def log_request():
    print(f"request: {request}")

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None

@app.route('/download/<filename>', methods=['GET'])
@auth.login_required
def download_file(filename):
    file_path = f"./files/{filename}"  
    try:
        return send_file(file_path, as_attachment=True) 
    except Exception as e:
        return jsonify({"error": str(e)}), 404  

@app.route('/test/bdc', methods=['POST'])
def post_data():
    # Get JSON data from the request body
    data = request.get_json()

    print(f"Received: {data}")

    # Send back the response as JSON
    return jsonify("response"), 200

@app.route('/test/bdc', methods=['PUT'])
def put_data():
    # Get JSON data from the request body
    data = request.get_json()
    print("put")
    print(data)

    # Send back the response as JSON
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

