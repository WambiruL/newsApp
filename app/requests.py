import urllib.request,json
from .models import Sources

api_key=None
s_url=None
art_url=None

def configure_request(app):
    global api_key,s_url
    api_key=app.config['API_KEY']
    s_url-app.config['NEWS_API_BASE_URL']
    art_url=app.config['NEWS_ARTICLES_API_URL']

def get_sources(category):
    """
    function that gets response from the api call
    """    
    sources_url = s_url.format(category,api_key)

    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        response = json.loads(sources_data)

        sources_outcome = None

        if response['sources']:
            sources_outcome_items = response['sources']
            sources_outcome = process_new_sources(sources_outcome_items)
    return sources_outcome 

def process_new_sources(sources_list):
    sources_outcome = []

    for one_source in sources_list:
        id = one_source.get("id")
        name = one_source.get("name")
        description = one_source.get("description")
        url = one_source.get("url")
        category = one_source.get("category")
        language = one_source.get("language")
        country = one_source.get("country")
        
        new_source = Sources(id,name,description,url,category,language,country)
        sources_outcome.append(new_source)
    
    return sources_outcome

def get_articles(article):

    articles_url = art_url.format(article,api_key)
    with urllib.request.urlopen(articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_outcome = None

        if articles_response['articles']:
            articles_outcome_items = articles_response['articles']
            articles_outcome = process_new_articles(articles_outcome_items)
    return articles_outcome