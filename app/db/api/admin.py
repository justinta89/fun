from app.db.model import UserAdmin, get_session


class Admin:

    def get_username(user):
        session = get_session()
        admin = session.query(UserAdmin).first()
        if user == admin.username:
            return True

    def get_password(passwd):
        session = get_session()
        admin = session.query(UserAdmin).first()
        if passwd == admin.password:
            return True