from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    path = db.Column(db.String(200))

    def __repr__(self):
        return f"<Video {self.title}>"
