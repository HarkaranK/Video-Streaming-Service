from flask import Flask, jsonify, render_template, send_file  
from flask_sqlalchemy import SQLAlchemy
from models import db 
from models import Video

app = Flask(__name__)

# Configure MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://vid:vid@video-streaming-service-mysql-1:3306/video'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/videos-page', methods=['GET'])
def render_video_page():
    videos = Video.query.all()
    return render_template('base.html', videos=videos)

@app.route('/videos/<int:video_id>', methods=['GET'])
def stream_video(video_id):
    video = Video.query.get(video_id)
    if video:
        # video_path = f"/files/{video.path}" 
        # video_path = f"/app/files/{video.path}" 
        video_path = video.path
        #video_path = video.path  # Assuming this is the path to the video file
        # Implement logic to retrieve the video file and stream it
        # You can use send_file from Flask to stream the file
        return send_file(video_path, as_attachment=False)
    else:
        return "Video not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

