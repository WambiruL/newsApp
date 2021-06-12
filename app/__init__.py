from flask import Flask
from flask_bootstrap import Bootstrap


#initialize application
app= Flask(__name__)

#initialize flask extensions
bootstrap= Bootstrap(app)

from app import  views