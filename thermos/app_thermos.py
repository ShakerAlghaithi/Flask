import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy  #pip install flask-sqlalchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY']= '\x85\x8a\x15\x8f\x8a\xe1\x0e\xca\x1b\\\xf1\xb7\xb8\xc7\xb5\x13\x1c\xe8s\x83\xb8\xfa\xe0\xb9'
# setup sqlite for database and configuring the connection to it
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

#removing old method
# def store_bookmark(url, description):
#     bookmarks.append(dict(
#         url=url,
#         description=description,
#         user= "Alghaithi",
#         date= datetime.utcnow()
#
#     ))

# def new_bookmarks(num):
#     return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]
from forms import BookmarkForm
import models 

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html', new_bookmarks=models.Bookmark.newest(5))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():  #check if the form has been submitted of filled
        url = form.url.data
        description = form.description.data
        bm = models.Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash("Stored bookmark: '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
if __name__== "__main__":
    app.run(debug=True)
