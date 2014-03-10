from app import db, app
from sqlalchemy import asc
from hashlib import md5
from datetime import date, datetime


class userAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30), unique=True, nullable=False)
    passwd = db.Column(db.String(50), nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return "user {0}".format(self.uname)


# This adds the ability for me to have an avatar on my page. Needs to be in a
# class called in the layout.html page.
# def avatar(self, size):
#    return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() +\
# '?d=mm&s=' + str(size)

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    title = db.Column(db.String)
    timestamp = db.Column(db.DateTime)

    def day(self, timestamp):
        day = date.today()
        tday = day.strftime("%A %d, %B %Y")
        return tday

    def __repr__(self):
        return "{0}".format(self.body)