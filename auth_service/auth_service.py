from flask import Flask, request, jsonify

app = Flask(__name__)

USERS = {
    "username": "password"  # Add more users as needed
}

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if USERS.get(username) == password:
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5002)