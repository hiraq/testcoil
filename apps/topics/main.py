from http import HTTPStatus
from pymongo.errors import OperationFailure

from sanic.response import json
from sanic import Blueprint

blueprint = Blueprint('topic_app')
