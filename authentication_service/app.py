from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Check if the provided credentials are correct
    if username == "admin" and password == "password":
        # If credentials are correct, redirect to http://localhost:8001/
        return redirect('http://localhost:8001/')
    
    # If credentials are invalid, stay on the login page
    return render_template('login.html', message="Invalid credentials")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
