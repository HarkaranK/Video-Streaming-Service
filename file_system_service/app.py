from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def save_file():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join("./data", filename))
    return "Saved"

@app.route('/download/<filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory('./data', filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

