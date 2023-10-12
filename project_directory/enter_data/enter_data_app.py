from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@mysql_db/dataDB'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))

@app.route('/')
def index():
    return render_template('enter_data.html')

@app.route('/data', methods=['POST'])
def enter_data():
    content = request.json['content']
    data = Data(content=content)
    db.session.add(data)
    db.session.commit()
    return jsonify({"message": "Data entered successfully!"}), 200

if __name__ == '__main__':
    with app.app_context():  # Using application context
        db.create_all()
    app.run(host='0.0.0.0', port=8000)
