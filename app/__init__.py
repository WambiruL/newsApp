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

    return app