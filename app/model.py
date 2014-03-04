from app import db


class userAdmin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    uname = db.Column(db.String(30), unique = True, nullable = False)
    passwd = db.Column(db.String(50), nullable = False)

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