from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        msg = 'Login Requested for OpenID=' + form.openid.data + ', Remember Me=' + str(form.remember_me.data)
        flash(msg)
        return redirect('/index')
    return render_template('login.html.j2',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])