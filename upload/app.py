from flask import Flask, request, jsonify, render_template
import os
import requests

app = Flask(__name__)

#UPLOAD_FOLDER = '/path/to/your/upload/directory'  # Specify your upload directory path

@app.route('/upload', methods=['GET'])
def render_upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['file']

    # Send the file to the File System service
    files = {'file': (file.filename, file.stream, file.mimetype)}
    response = requests.post('http://127.0.0.1:5003/receive_file', files=files) # Works when not containerized
    # response = requests.post('http://video-streaming-service-filesystem-1:5003/receive_file', files=files)
    # response = requests.post('http://192.168.128.4:5003/receive_file', files=files)

    if response.status_code == 200:
        return jsonify({'message': 'File uploaded successfully'}), 200
    else:
        return jsonify({'message': 'File upload failed'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)


