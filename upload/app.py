# Simplified version; integrate with authentication and database.
from flask import Flask, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']

    # Save to filesystem service
    response = requests.post('http://filesystem:5000/upload', files={'file': file})
    return response.json(), response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0')
