from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mingming'}
    posts = [
        {
            'author' : {'nickname': 'Ming'},
            'body' : 'Beautiful day in Portland!'
        },
        {
            'author' : {'nickname': 'Wang'},
            'body' : 'The Avengers movie was so cool!'
        }
    ]

    return render_template("index.html",
        title = "Home",
        user = user,
        posts = posts)
