from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymongo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@mysql_db/dataDB'
db = SQLAlchemy(app)

mongo_client = pymongo.MongoClient("mongodb://mongo_db:27017/")
mongo_db = mongo_client["resultsDB"]
mongo_col = mongo_db["datas"]

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))

@app.route('/analytics', methods=['GET'])
def get_analytics():
    all_data = Data.query.all()
    # Sample: Calculate the count of entries
    count = len(all_data)
    # Push to Mongo
    result_data = {
        "count": count
    }
    mongo_col.insert_one(result_data)
    
    return jsonify(result_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)
