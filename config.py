import os
class Config:
    """
    General configuration parent class
    """
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS=True


    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    """
    Production configuration child class

    Args:
    Config: The parent confiuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI ='postgres://agpkhjojlojhcf:05374d97f25a8737b836d9397988b945ce99a0e65599c06df3943b4e54a67129@ec2-54-165-36-134.compute-1.amazonaws.com:5432/d5gj0bl8db7t0c'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:software112@localhost/pitches'

    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:software112@localhost/pitches'
    DEBUG = True


config_options={
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
