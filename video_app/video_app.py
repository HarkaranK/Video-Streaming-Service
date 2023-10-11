from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

AUTH_SERVICE_URL = "http://auth_service:5002/authenticate"
FILE_SERVICE_URL = "http://filesystem:5001"

@app.route('/upload', methods=['POST'])
def upload_video():
    auth_data = {"username": request.form["username"], "password": request.form["password"]}
    auth_response = requests.post(AUTH_SERVICE_URL, json=auth_data)
    
    if auth_response.status_code == 200:
        file = request.files['file']
        if file:
            response = requests.post(FILE_SERVICE_URL + "/upload", files={"file": file})
            return jsonify(response.json()), 200
    return jsonify({"status": "error", "message": "Upload failed"}), 400

@app.route('/stream/<filename>', methods=['GET'])
def stream_video(filename):
    return redirect(FILE_SERVICE_URL + f"/download/{filename}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)