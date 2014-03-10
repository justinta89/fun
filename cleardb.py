from app import db, model


def cleardb():
    posts = model.Post.query.all()
    for p in posts:
        db.session.delete(p)

    db.session.commit()


if __name__ == '__main__':
    cleardb()
