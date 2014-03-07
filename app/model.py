from app import db, app
from hashlib import md5


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
    timestamp = db.Column(db.String)

    def __repr__(self):
        return "{0}".format(self.body)





"""
class Port(Base):
        __tablename__   = 'port'
        id                              = Column(Integer, primary_key=True)
        server_id               = Column(Integer, ForeignKey('server.id'))
        port_number             = Column(Integer)
        protocol                = Column(String)
        banner                  = Column(String)

class Server(Base):
        __tablename__   = 'server'
        id                              = Column(Integer, primary_key=True)
        project_id              = Column(Integer, ForeignKey('project.id'))
        ip                              = Column(String)
        domain                  = Column(String)
        segment_name    = Column(String)
        ports                   = relation(Port)"""