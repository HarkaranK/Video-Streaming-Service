from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "user": "pass"
}

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if users.get(username) == password:
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "failure"}), 401
