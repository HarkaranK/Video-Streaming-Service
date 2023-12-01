from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL connection
# Replace 'root', 'vid', 'host.docker.internal', '3306', 'videos' with your MySQL details
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:vid@host.docker.internal:3307/videos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking as it can be resource-intensive
db = SQLAlchemy(app)

# Define your database model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    path = db.Column(db.String(200))

    def __repr__(self):
        return f"<Video {self.title}>"

# Example route to fetch videos from the database
@app.route('/videos')
def get_videos():
    videos = Video.query.all()
    video_list = [{'id': video.id, 'title': video.title, 'path': video.path} for video in videos]
    return jsonify({'videos': video_list})

if __name__ == '__main__':
    app.run(debug=True)
