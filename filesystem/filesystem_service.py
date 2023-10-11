from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

FILE_DIR = "files"

if not os.path.exists(FILE_DIR):
    os.makedirs(FILE_DIR)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join(FILE_DIR, file.filename)
        file.save(filepath)
        return {"status": "success", "path": filepath}, 200
    return {"status": "error", "message": "No file provided"}, 400

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(FILE_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True, port=5001)