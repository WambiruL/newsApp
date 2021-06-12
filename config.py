import os

class Config:
    '''
    General configuration parent class
    '''
    API_KEY=os.environ.get("API_KEY")
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&apiKey=ded7a04297794b6b8499160ed51d1a2c'
    NEWS_ARTICLES_APL_URL='https://newsapi.org/v2/everything?q={}&apiKey=ded7a04297794b6b8499160ed51d1a2c'
    SOURCE_ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apiKey=ded7a04297794b6b8499160ed51d1a2c'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig
}
