# This is a very basic file service for the sake of example. In a real-world scenario, more robustness is needed.
from flask import Flask, request, send_from_directory

app = Flask(__name__)

UPLOAD_FOLDER = '/videos'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return jsonify({"status": "success", "path": os.path.join(UPLOAD_FOLDER, file.filename)}), 200

@app.route('/<filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
