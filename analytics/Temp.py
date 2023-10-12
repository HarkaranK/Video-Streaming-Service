from sqlalchemy import Column, Integer, String, Time, Date
from base import Base

class Temp(Base):
    __tablename__ = "temp"

    id = Column(Integer, primary_key=True, autoincrement=True)
    weather = Column(String(40), nullable=False)
    time_of_day = Column(Time, nullable=False)
    day_month = Column(Date, nullable=False)


    def __init__(self, weather, time_of_day, day_month):
        self.weather = weather
        self.time_of_day = time_of_day
        self.day_month = day_month

    def to_dict(self):
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['weather'] = self.weather
        my_dict['time_of_day'] = self.time_of_day
        my_dict['day_month'] = self.day_month
        return my_dict