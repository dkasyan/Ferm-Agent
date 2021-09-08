import datetime
import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    sensor_type = db.Column(db.String(80), nullable=False)
    sensor_value = db.Column(db.Text, nullable=False)
    online_status = db.Column(db.Boolean, default=False)