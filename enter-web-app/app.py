from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from Temp import Temp
from flask import Flask, render_template, request
from TempForm import TempForm
import request

DB_HOST = 'entry_db'
DB_PORT = '3306'
DB_USER = 'temp_app'
DB_PASSWORD = 'temp_app'
DB_NAME = 'temp_app'

DB_ENGINE = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
Base.metadata.bind = DB_ENGINE
Session = sessionmaker(bind=DB_ENGINE)

app = Flask(__name__)

@app.route('/enter-web-app', methods=['GET', 'POST'])
def enter_temp():

    form = TempForm(request.form)
    if request.method == "POST":
        if form.validate():
            tem = Temp(form.weather.data, form.time_of_day.data, form.day_month.data)
            session = Session()
            session.add(tem)
            session.commit()
            session.close()

            session = DB_SESSION()
            tempQ = session.query(Temp).all()
            session.close()
            temps = []
            for tem in tempQ:
                temps.append(temp.to_dict())

            requests.get('http://analytics:8100/update_stats')
            return render_template('index.html', existing_temps=temps)

        session = DB_SESSION()
        tempQ = session.query(Temp).all()
        session.close()
        temps = []
        for tem in tempQ:
            temps.append(temp.to_dict())

        return render_template('index.html',existing_temps=temp)


if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0')