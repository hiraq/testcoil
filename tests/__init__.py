from sanic import Sanic

from core.extentions.exceptions import blueprint as ext_exceptions
from core.extentions.middlewares import blueprint as ext_middlewares

from mongoengine import connect as mongo_conn
from apps.commons.exceptions import blueprint as common_exceptions

from apps.ping import blueprint as ping_app
from apps.news import blueprint as news_app
from apps.topics import blueprint as topic_app

def build_full_app(settings={}):
    """Build Sanic Full App

    Mirroring main.py

    Args:
        settings = A dictionary of application settings (optional)

    Returns:
        A sanic app
    """
    app = Sanic('test')

    # only updating settings if given settings
    # has values
    if isinstance(settings, dict):
        if len(settings.keys()) >= 1:
            app.config.update(settings)

    app.blueprint(ext_exceptions)
    app.blueprint(ext_middlewares)
    app.blueprint(common_exceptions)

    app.blueprint(ping_app, url_prefix='/ping')
    app.blueprint(news_app, url_prefix='/v1/news')
    app.blueprint(topic_app, url_prefix='/v1/topics')

    mongo_conn(host=app.config.get('MONGO_HOST'))
    return app
