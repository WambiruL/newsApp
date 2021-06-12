from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig


#initialize application
app= Flask(__name__)

#initialize flask extensions
bootstrap= Bootstrap(app)

#setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import  views