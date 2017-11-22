from app import db
from hashlib import md5

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String)
    title = db.Column(db.String(140))
    description = db.Column(db.String(1024))
    expiration = db.Column(db.DateTime)
    locationx = db.Column(db.Float)
    locationy = db.Column(db.Float)
