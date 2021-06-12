from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap=Bootstrap()

def create_app(config_name):
#initialize application
    app= Flask(__name__)

#initialize flask extensions
    bootstrap.init_app(app)

#setting up app configuration
    app.config.from_object(config_options[config_options])

#Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)


    return app