from src.models import models
from src.database import db
import os


os.environ['ENV_CONFIG'] = 'LoadDataConfig'

# workaround for PEP-8
if True:
    from src.app import app

if __name__ == '__main__':
    with app.app_context():
        u = models.User(name='foo')
        db.session.add(u)
        db.session.commit()
