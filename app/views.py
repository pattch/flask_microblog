from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import LoginForm
from .models import User

@lm.user_loader
def user_loader(user_id):
    # Given a User ID, return the correct User
    return User.query.get(int(user_id))

@app.before_request
def before_request():
    g.user = current_user

# Route DECORATORS -- Decorate the index function, adding Flask Functionality
@app.route('/')
@app.route('/index')
@login_required
def index():
    # user = {'nickname': 'Miguel', 'id': 99999}
    user = g.user
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
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        remember_me = form.remember_me.data
        # session['remember_me'] = remember_me
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if user and password and user.password == password:
            login_user(user, remember_me)
            return redirect(request.args.get('next') or url_for('index'))
        flash('Invalid Login Information.')
        return redirect(url_for('index'))
    return render_template('login.html.j2',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))