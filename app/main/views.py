from flask import render_template
from . import main

#views
@main.route('/')
def homepage():

    """
     Views thats renders news sources to the home page
    """

    return render_template("sources.html")