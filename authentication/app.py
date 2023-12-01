from flask import Flask, request, jsonify, redirect, render_template

app = Flask(__name__)

users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        # Authentication successful, redirect to the index page
        return redirect('http://127.0.0.1:5002/upload') 
    else:
        # Authentication failed, render the login page again with a message
        return redirect('/', message='Invalid credentials. Please try again.')


# @app.route('/index')
# def index():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)