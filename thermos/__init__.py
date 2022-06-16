import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY']= '\x85\x8a\x15\x8f\x8a\xe1\x0e\xca\x1b\\\xf1\xb7\xb8\xc7\xb5\x13\x1c\xe8s\x83\xb8\xfa\xe0\xb9'
# setup sqlite for database and configuring the connection to it
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['DEBUG']
db = SQLAlchemy(app)

import models
import views
