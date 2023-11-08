from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'jdhgky38975985692-$#^$&^%$^%##%@$%^&*(&^%$%^&*()*&^%$'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/thuchanh3?charset=utf8mb4" % quote(
    'Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)