from flask import render_template
from ..requests import get_sources,get_articles
from . import main


#views
@main.route('/')
def homepage():

    """
     Views thats renders news sources to the home page
    """

    general_news=get_sources('general')
    business_news=get_sources('business')
    sports_news=get_sources('sports')
    return render_template('sources.html',general=general_news, business=business_news, sports=sports_news)


@main.route('/News-Articles')
def NewsArticles():
    """
    View that would return news articles
     
    """
    health_articles = get_articles('health')
    education_articles = get_articles('technology')
    return render_template('articles.html',health=health_articles, tech =education_articles)