from flask import jsonify, request, abort
from app import app, db
from datetime import datetime
from .models import Listing

date_format = "%Y-%m-%dT%H:%M:%S"

# APIs for Collections of Listings
@app.route('/api/listings', methods=['GET','POST','DELETE'])
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
        return jsonify({'id':id})
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
