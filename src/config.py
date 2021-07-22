import os


class Config(object):
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}/postgres'.format(**{
        'user': os.getenv('DB_USER', 'postgres'),
        'password': os.getenv('DB_PASSWORD', 'postgres'),
        'host': os.getenv('DB_HOST', 'localhost'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(Config):
    # Flask
    DEBUG = True

class LoadDataConfig(Config):
    # Flask
    DEBUG = False
    USE_RELOADER = False
