from app import db
from hashlib import md5

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def is_active(self):
        # All Users are Active Currently
        return True

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        # No Current Support or Need for Anonymity
        return False

    # Gravatar Avatar, Uses md5 of Email and Pixel Size, Returns an Image
    def avatar(self,size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    body = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
