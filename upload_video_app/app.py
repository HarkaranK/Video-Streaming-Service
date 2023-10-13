from flask import Flask, render_template, request, redirect, url_for, flash
import os

UPLOAD_FOLDER = 'uploaded_videos'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'flv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'some_secret_key'

# Check if uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_page():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'videoFile' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['videoFile']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        flash('Video successfully uploaded')
        return redirect('http://localhost:8001/')  # Redirect to the desired URL
    else:
        flash('Allowed video types are -> mp4, avi, mkv, flv')
        return redirect(request.url)

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', debug=True)
