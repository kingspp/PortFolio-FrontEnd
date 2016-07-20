from src.webapp_flask import app,_data
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1/portfolio'
db = SQLAlchemy(app)

class Timeline(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True,autoincrement=True)
    date = db.Column(db.VARCHAR(20), unique=True, nullable=False)
    header = db.Column(db.TEXT, nullable=False)
    body = db.Column(db.TEXT, nullable=False)

    def __init__(self, date, header, body):
        self.date = date
        self.header = header
        self.body = body

    def __repr__(self):
        return [self.date, self.header, self.body].__str__()

#db.create_all()
# for entry in _entries:
#     db.session.add(entry)
# db.session.commit()

_data = Timeline.query.all()