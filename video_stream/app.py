from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:vid@host.docker.internal:3307/videos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define your database model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    path = db.Column(db.String(200))

    def __repr__(self):
        return f"<Video {self.title}>"

# Route to fetch uploaded videos from the database
@app.route('/videos', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    video_list = [{'id': video.id, 'title': video.title, 'path': video.path} for video in videos]
    return jsonify({'videos': video_list})

@app.route('/videos-page', methods=['GET'])
def render_video_page():
    # Assuming you have an existing HTML file named 'video_list.html'
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

