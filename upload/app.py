from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import requests
from models import db 
from models import Video


app = Flask(__name__)

# Configure MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://vid:vid@video-streaming-service-mysql-1:3307/video'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking as it can be resource-intensive

# Initialize SQLAlchemy
db = SQLAlchemy(app)


@app.route('/upload', methods=['GET'])
def render_upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    # Send the file to the File System service
    files = {'file': (file.filename, file.stream, file.mimetype)}
    response = requests.post('http://video-streaming-service-filesystem-1:5003/receive_file', files=files)

    if response.status_code == 200:
        # If file upload is successful, save metadata to MySQL database
        video = Video(title=file.filename, path=f'../filesystem/files/{file.filename}')
        db.session.add(video)
        db.session.commit()
        
        return jsonify({'message': 'File uploaded successfully'}), 200
    else:
        return jsonify({'message': 'File upload failed'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)



