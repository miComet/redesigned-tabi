import os

os.environ['ENV_CONFIG'] = 'DevelopmentConfig'

# workaround for PEP-8
if True:
    from src.app import app

if __name__ == '__main__':
    app.run()
