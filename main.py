import argparse
from mongoengine import connect as mongo_conn
from sanic import Sanic

from core.extentions.exceptions import blueprint as ext_exceptions
from core.extentions.middlewares import blueprint as ext_middlewares

from apps.commons.exceptions import blueprint as common_exceptions

from apps.ping import blueprint as ping_app
from apps.news import blueprint as news_app

from settings import Settings

# Command line parser options & setup default values
parser = argparse.ArgumentParser()
parser.add_argument('--host', help='Setup host ip to listen up, default to 0.0.0.0', default='0.0.0.0')
parser.add_argument('--port', help='Setup port to attach, default to 8080', default='8080')
parser.add_argument('--workers', help='Setup workers to run, default to 1', type=int, default=1)
parser.add_argument('--debug', help='Enable or disable debugging', action='store_true')
parser.add_argument('--accesslog', help='Enable or disable access log', action='store_true')
args = parser.parse_args()

# Configure Sanic apps
app = Sanic(__name__)
app.config.from_object(Settings())

# Install extentions
app.blueprint(ext_exceptions)
app.blueprint(ext_middlewares)

# Common things
app.blueprint(common_exceptions)

# Install apps
app.blueprint(ping_app, url_prefix='/ping')
app.blueprint(news_app, url_prefix='/v1/news')

# Running sanic, we need to make sure directly run by interpreter
# ref: http://sanic.readthedocs.io/en/latest/sanic/deploying.html#running-via-command
if __name__ == '__main__':
    # connect to mongodb
    mongo_conn(host=app.config.get('MONGO_HOST'))

    app.run(
        host=args.host, 
        port=args.port, 
        workers=args.workers, 
        debug=args.debug, 
        access_log=args.accesslog
    )
