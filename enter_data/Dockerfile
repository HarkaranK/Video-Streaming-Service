FROM python:3.8

WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install --upgrade Flask Jinja2

ADD . /app/

CMD ["python", "enter_data_app.py"]
