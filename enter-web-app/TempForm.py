from wtforms import Form, StringField, FloatField, validators, TimeField, DateField




class TempForm(Form):
    weather = StringField('Weather', [validators.Length(min=1, max=40)])
    time_of_day = TimeField('Time of Day', [validators.DataRequired()])
    day_month = DateField('Day and Month', [validators.DataRequired()])

    