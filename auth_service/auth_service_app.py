
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample users for demonstration
USERS = {
    "username1": "password1",
    "username2": "password2"
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def authenticate():
    username = request.json['username']
    password = request.json['password']
    
    if username in USERS and USERS[username] == password:
        # return jsonify({"message": "Authenticated!"}), 200
        return render_template('authenticated.html')
    else:
        return jsonify({"message": "Authentication failed!"}), 401

@app.route('/authenticated')
def authenticated():
    return render_template('authenticated.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)