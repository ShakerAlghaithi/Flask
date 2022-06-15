# use pip install flask-wtf command to make it work
#from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms.fields import StringField
#from flask.ext.wtf.html5 import URLField
#from flask_wtf.html5 import URLField
from wtforms import URLField
from wtforms.validators import DataRequired, url

class BookmarkForm(FlaskForm):
    url= URLField('The URL for your bookmark: ', validators=[DataRequired(), url()])
    description = StringField('Add an optional description: ')
#checking if the url start with http or https and description field is not empty by calling the validate function
    def validate(self):
        if not self.url.data.startswith("http://") or\
           self.url.data.startswith("https://"):
           self.url.data = "http://" + self.url.data

        if not FlaskForm.validate(self):
            return False

        if not self.description.data:
            self.description.data = self.url.data
        return True
