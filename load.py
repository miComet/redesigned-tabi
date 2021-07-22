from src.models import models
from src.database import db
import os


os.environ['ENV_CONFIG'] = 'LoadDataConfig'

if __name__ == '__main__':
    from src.app import app
    with app.app_context():
        u = models.User(name='foo')
        db.session.add(u)
        db.session.commit()

