from mongoengine import connect
from statistics import Result, CourseStats 
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from Temp import Temp
from flask import Flask





SQL_HOST = 'entry_db'
SQL_PORT = '3306'
SQL_USER = 'temp_app'
SQL_PASSWORD = 'temp_app'
SQL_DB_NAME = 'temp_app'

DB_ENGINE = create_engine(f"mysql+pymysql://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DB_NAME}")

Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

MONGO_HOST = 'results_db'
MONGO_PORT = '27017'
MONGO_DB_NAME = 'temp_app'
CONN_STR = f'mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB_NAME}'

connect(host=CONN_STR)

app = Flask(__name__)

@app.route('/update_stats', methods=['GET'])
def update_stats():
    #If there was no previous record
    # The last temp is set to 0
    if len(Results.objects()) > 0:
        previous_results = list(Results.objects())[-1]
        previouse_temp = previous_results.Wtype
    else:
        previouse_temp = 0
    
    session = DB_SESSION()
    tempQ - session.query(Temp).all()
    session.close()

    num_Wtype = len(Wtype)

    # Do something after

    return '200'
    




if __name__ == "__main__":
    app.run(port=8100, host='0.0.0.0')