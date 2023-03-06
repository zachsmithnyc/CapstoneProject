import os
from flask import Flask

'''
The application factory creates and configures the app
'''

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'inventr.sqlite')
    )

    if test_config is None:
        # loads the instance config for dev
        app.config.from_pyfile('config.py', silent=True)
    else:
        # loads the test config
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello World!'
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)


    return app