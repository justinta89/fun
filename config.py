

class Config(object):
    DEBUG = False
    CSRF_ENABLED = True


class Dev(Config):
    DEBUG = True
    SECRET_KEY = "devKey"


class Production(Config):
    SECRET_KEY = '\xf2\xd6\xea\xd83\x03yg\x0e\x1e=}$\xd6\x02`\xc8e>\x8c'