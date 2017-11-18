from flask import render_template
from app import app

# Route DECORATORS -- Decorate the index function, adding Flask Functionality
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel', 'id': 99999}
    posts = [
        {
            'author': {'nickname': 'John', 'id':12345},
            'body': 'Blog post by John Man'
        },
        {
            'author': {'nickname': 'Susan Be Anthony', 'id': 67890},
            'body': 'Coming out as Trans, call me Andy'
        }
    ]
    return render_template('index.html.j2',
            user=user,
            posts=posts)