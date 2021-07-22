import os

os.environ['ENV_CONFIG'] = 'DevelopmentConfig'

if __name__ == '__main__':
    from src.app import app
    app.run()
