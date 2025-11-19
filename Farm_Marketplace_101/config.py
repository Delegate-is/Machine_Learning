import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'instance', 'farm.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', os.path.join(basedir, 'static', 'uploads'))
ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}
# MPESA
MPESA_CONSUMER_KEY = os.environ.get('MPESA_CONSUMER_KEY')
MPESA_CONSUMER_SECRET = os.environ.get('MPESA_CONSUMER_SECRET')
MPESA_SHORTCODE = os.environ.get('MPESA_SHORTCODE')
MPESA_PASSKEY = os.environ.get('MPESA_PASSKEY')
MPESA_ENV = os.environ.get('MPESA_ENV','sandbox') # sandbox or production


class ProdConfig(Config):
pass


class DevConfig(Config):
DEBUG = True