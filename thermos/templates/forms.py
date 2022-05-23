# use pip install flask-wtf command to make it work 
from flask_wtf import form
from wtforms.fields import StringField
from flask.ext.wtf.html5 import URLField
from wtforms.validators import DataRequired, url

class bookmarkForm(Form):
    url= URLField('url', validators=[DataRequired(), url()])
    description = StringField('description')
