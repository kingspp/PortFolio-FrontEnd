from flask_httpauth import HTTPBasicAuth
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from flask import request
import logging
from flask import Flask
import argparse
import os
import configparser
from flask_sqlalchemy import SQLAlchemy
config = configparser.RawConfigParser()
config.read('src/static/app.config.properties')

# Logging Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask Configuration
app = Flask(__name__, static_folder=str(os.getcwd()+'/'+config.get('ServerConfiguration','flask.staticfiles')))
auth = HTTPBasicAuth()
app.secret_key = 'some_secret'

users = {
    "admin": "admin@123"
}


#DB Configuration
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






# Flask Routing
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route("/")
@auth.login_required
def login():
    user = auth.username()
    flash('Welcome %s', user)
    return render_template('index.html')

# Main Function - Start Here
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flask Example: Python Webapp')
    parser.add_argument('-r', help="Run Flask", default=False, action="store_true")
    args = vars(parser.parse_args())
    if args['r']:   
        app.run(host='localhost', port=int(config.get('ServerConfiguration','flask.port')), debug=True)
