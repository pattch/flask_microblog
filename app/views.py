from flask import jsonify, request, abort
from app import app, db
from datetime import datetime
from .models import Listing

date_format = "%Y-%m-%dT%H:%M:%S"

# APIs for Collections of Listings
@app.route('/api/listings/', methods=['GET','POST','DELETE'])
def listings():
    if request.method == 'GET':
        return get_listings()
    elif request.method == 'POST':
        return create_listing()
    elif request.method == 'DELETE':
        return delete_all()
    abort(404)

# Convert a listing to a format that can be jsonified
def jsonify_listing(listing):
    return {
        'id': listing.id,
        'user': listing.user,
        'title': listing.title,
        'description': listing.description,
        'expiration': get_str_from_datetime(listing.expiration),
        'location': {
            'x': listing.locationx,
            'y': listing.locationy
        }
    }

# Return a list of all Listings in the DB
def get_listings():
    listings = Listing.query

    active = request.args.get('active')
    if active and active == '1':
        listings = listings.filter(Listing.expiration > datetime.utcnow())

    page,length = request.args.get('page'),request.args.get('length')
    if page and length:
        try:
            page,length = int(page),int(length)
            start,end = ((page - 1) * length) + 1, ((page) * length) + 1
            print(start,end)
            listings = listings.filter(Listing.id.in_(range(start,end)))
        except BaseException as error:
            print(error)
            abort(400)

    listings = listings.all()
    json_listings = jsonify([jsonify_listing(x) for x in listings])
    return json_listings

def get_datetime_from_str(date_str):
    return datetime.strptime(date_str,date_format)

def get_str_from_datetime(date_time):
    return date_time.strftime(date_format)

def create_listing_from_json(content):
    expiration = get_datetime_from_str(content['expiration'])
    user,title,description = content['user'],content['title'],content['description']
    x,y = content['location']['x'],content['location']['y']
    l = Listing(user=user,title=title,description=description,expiration=expiration,locationx=x,locationy=y)
    return l

def create_listing():
    try:
        content = request.get_json(force=True)
        l = create_listing_from_json(content)
        db.session.add(l)
        db.session.commit()
        return jsonify({'id':l.id})
    except BaseException as error:
        print(error)
        abort(400)

def delete_all():
    deleted_count = Listing.query.delete()
    if deleted_count:
        db.session.commit()
    return ('',204)

# APIs for Individual Listings
@app.route('/api/listings/<id>', methods=['GET','PUT','DELETE'])
def listing(id):
    try:
        id = int(id)
    except:
        abort(400)

    if request.method == 'GET':
        return get_listing(id)
    elif request.method == 'PUT':
        return update_listing(id)
    elif request.method == 'DELETE':
        return delete_listing(id)
    abort(404)

def get_listing(id):
    listing = Listing.query.get(id)
    if not listing:
        abort(404)

    return jsonify(jsonify_listing(listing))

# Simply Update Each Parameter
def update_listing(id):
    try:
        content = request.get_json(force=True)
        updated_fields = {
            'id': id,
            'user': content['user'],
            'title': content['title'],
            'description': content['description'],
            'expiration': get_datetime_from_str(content['expiration']),
            'locationx': content['location']['x'],
            'locationy': content['location']['y']
        }
        Listing.query.with_for_update().filter_by(id=id).update(updated_fields)
        db.session.commit()
        return ('',204)
    except BaseException as error:
        print(error)
        abort(400)

def delete_listing(id):
    listing = Listing.query.get(id)
    if listing is None:
        return ('',204)
    db.session.delete(listing)
    db.session.commit()
    return ('',204)



# @lm.user_loader
# def user_loader(user_id):
#     # Given a User ID, return the correct User
#     return User.query.get(int(user_id))
#
# @app.before_request
# def before_request():
#     g.user = current_user
#     if g.user.is_authenticated:
#         g.user.last_seen = datetime.utcnow()
#         db.session.add(g.user)
#         db.session.commit()
#
# # Route DECORATORS -- Decorate the index function, adding Flask Functionality
# @app.route('/')
# @app.route('/index')
# @login_required
# def index():
#     # user = {'nickname': 'Miguel', 'id': 99999}
#     user = g.user
#     posts = [
#         {
#             'author': {'nickname': 'John', 'id':12345},
#             'body': 'Blog post by John Man'
#         },
#         {
#             'author': {'nickname': 'Susan Be Anthony', 'id': 67890},
#             'body': 'Coming out as Trans, call me Andy'
#         },
#         {
#             'author': {'nickname': 'Sam', 'id': 1},
#             'body': 'HARD CODED YO'
#         }
#     ]
#     return render_template('index.html.j2',
#             user=user,
#             posts=posts)
#
# @app.route('/login', methods=['GET','POST'])
# def login():
#     if g.user is not None and g.user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         remember_me = form.remember_me.data
#         # session['remember_me'] = remember_me
#         email = form.email.data
#         password = form.password.data
#         user = User.query.filter_by(email=email).first()
#
#         if user and password and user.password == password:
#             login_user(user, remember_me)
#             return redirect(request.args.get('next') or url_for('index'))
#         flash(unicode('Invalid Login Information.'))
#         return redirect(url_for('index'))
#     return render_template('login.html.j2',
#             title='Sign In',
#             form=form,
#             providers=app.config['OPENID_PROVIDERS'])
#
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
#
# @app.route('/user/<nickname>')
# @login_required
# def user(nickname):
#     user = User.query.filter_by(nickname=nickname).first()
#     if not user:
#         flash(unicode('User %s not found.' % nickname))
#         redirect(url_for('index'))
#     posts = [
#         {'author': user, 'body': 'Test post 1'},
#         {'author': user, 'body': 'Test post 2'}
#     ]
#     return render_template('user.html.j2',
#             user=user,
#             posts=posts)
#
# @app.route('/edit', methods=['GET','POST'])
# @login_required
# def edit():
#     form = EditForm()
#     if form.validate_on_submit():
#         g.user.nickname = form.nickname.data
#         g.user.about_me = form.about_me.data
#         db.session.add(g.user)
#         db.session.commit()
#         flash(unicode('Changes Saved Successfully!'))
#         return redirect(url_for('edit'))
#     else:
#         form.nickname.data = g.user.nickname
#         form.about_me.data = g.user.about_me
#     return render_template('edit.html.j2', form=form)
