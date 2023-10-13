from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def stream_page():
    return render_template('stream.html')

@app.route('/stream', methods=['GET'])
def stream_video():
    # logic to fetch and stream video
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')
