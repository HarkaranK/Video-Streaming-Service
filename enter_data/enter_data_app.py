from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@mysql_db/grades_app'

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(25), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    grade = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    return render_template('enter_data.html')

@app.route('/data', methods=['POST'])
def enter_data():
    data = request.get_json()
    new_data = Data(**data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"message": "Data entered successfully!"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000)
