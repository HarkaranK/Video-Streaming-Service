from flask import Flask, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import requests
from models import db 
from models import Video


app = Flask(__name__)

# Configure MySQL connection
# Old
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://vid:vid@video-streaming-service-mysql-1:3306/video'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://vid:vid@mysql-service:3306/video'
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
    # response = requests.post('http://video-streaming-service-filesystem-1:5003/receive_file', files=files)
    response = requests.post('http://my-flask-service-5003:5003/receive_file', files=files)
    # response = requests.post('http://my-flask-service-5003.default.svc.cluster.local/receive_file', files=files)
    # response = requests.post('http://127.0.0.1:5003/receive_file', files=files)


    if response.status_code == 200:
        video = Video(title=file.filename, path=f'/app/files/{file.filename}')
        db.session.add(video)
        db.session.commit()
        
        # return redirect('http://my-flask-service-5000:5000/videos-page')
        # return redirect('http://my-flask-service-5000.default.svc.cluster.local/videos-page')
        return redirect('http://127.0.0.1:5000/videos-page') #Local
    else:
        return jsonify({'message': 'File upload failed'}), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5002)



