# Simplified version; integrate with authentication and database.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # For simplicity, hardcoding a video path. In real-world, fetch from database.
    return render_template('index.html', video_url='http://filesystem:5000/sample.mp4')
