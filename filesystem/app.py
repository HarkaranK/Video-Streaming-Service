from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('/app/files')  # Directory to store uploaded files

@app.route('/receive_file', methods=['POST'])
def receive_file():
    ensure_directory(UPLOAD_FOLDER)  # Ensure the directory exists
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    uploaded_file = request.files['file']

    if uploaded_file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
    uploaded_file.save(file_path)
    
    return jsonify({'message': 'File received and stored successfully'}), 200

def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)

