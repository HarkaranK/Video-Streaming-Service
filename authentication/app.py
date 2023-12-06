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
        # return redirect('http://my-flask-service-5002:5002/upload') 
        return redirect('http://my-flask-service-5002.default.svc.cluster.local/upload')

    else:
        # Authentication failed, render the login page again with a message
        return render_template('login.html', message='Invalid credentials. Please try again.')



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)