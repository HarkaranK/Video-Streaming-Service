from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db 
from models import Video

app = Flask(__name__)

# Configure MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://vid:vid@video-streaming-service-mysql-1:3306/video'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



# Route to fetch uploaded videos from the database
# @app.route('/videos', methods=['GET'])
# def get_videos():
#     videos = Video.query.all()
#     video_list = [{'id': video.id, 'title': video.title, 'path': video.path} for video in videos]
#     return jsonify({'videos': video_list})

@app.route('/videos-page', methods=['GET'])
def render_video_page():
    videos = Video.query.all()
    # Assuming you have an existing HTML file named 'video_list.html'
    return render_template('base.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

