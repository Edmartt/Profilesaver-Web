import os
from flask import Flask

def create_app():
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'profile.sqlite'),
    )
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    from . import database as db
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    db.init_app(app)
    return app
