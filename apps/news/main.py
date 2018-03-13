from http import HTTPStatus
from pymongo.errors import OperationFailure

from sanic.response import json
from sanic import Blueprint

from apps.news import handlers

blueprint = Blueprint('news_app')
blueprint.add_route(handlers.create, '/', methods=['POST'])
