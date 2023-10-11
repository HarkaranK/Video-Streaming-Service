from flask import Flask, request, render_template_string, jsonify
import requests

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        # Save to filesystem service
        response = requests.post('http://filesystem:5002/upload', files={'file': file})
        return response.json(), response.status_code
    else:
        # Render a basic upload form for GET request
        return '''
        <html>
        <body>
            <form method="post" enctype="multipart/form-data" action="/upload">
                <input type="file" name="file">
                <input type="submit" value="Upload">
            </form>
        </body>
        </html>
        '''

if __name__ == "__main__":
    app.run(host='0.0.0.0')
