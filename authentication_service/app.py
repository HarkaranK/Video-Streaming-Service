from flask import Flask, request

app = Flask(__name__)

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "admin" and password == "password":
        return "Valid"
    return "Invalid", 401

if __name__ == "__main__":
    app.run(host='0.0.0.0')
