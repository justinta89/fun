from app.db.model import Post, get_session

session = get_session()


class Posts:

    def set_post(body, title, page, timestamp):
        post = Post(body, title, page, timestamp)
        session.add(post)
        session.commit()

    def get_post():
        pass

    def edit_post():
        pass

    def get_title():
        pass

    def get_body():
        pass

    def get_time():
        pass