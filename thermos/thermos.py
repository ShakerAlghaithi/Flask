from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import bookmarkForm

app = Flask(__name__)

# shouldn't use global list to store data, but i am using it for praticing at the moment.
bookmarks= []
app.config['SECRET_KEY']= '\x85\x8a\x15\x8f\x8a\xe1\x0e\xca\x1b\\\xf1\xb7\xb8\xc7\xb5\x13\x1c\xe8s\x83\xb8\xfa\xe0\xb9'
def store_bookmark(url):
    bookmarks.append(dict(
        url=url,
        user= "Alghaithi",
        date= datetime.utcnow()

    ))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]
@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))

@app.route('/add', methods=['GET', 'POST'])
def add():     
    form = bookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
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
