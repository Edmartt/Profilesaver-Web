import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    MYSQL_HOST=os.environ.get('HOST')
    MYSQL_USER=os.environ.get('USER')
    MYSQL_PASSWORD=os.environ.get('PASSWORD')
    MYSQL_DB= os.environ.get('DATABASE')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
        DEBUG = True
        SECRET_KEY=os.environ.get('SECRET_KEY') or 'dev'


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass

config = {
     'development': DevelopmentConfig,
     'testing': TestingConfig,
     'production': ProductionConfig,
     'default': DevelopmentConfig
}

