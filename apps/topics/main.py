from http import HTTPStatus
from pymongo.errors import OperationFailure

from sanic.response import json
from sanic import Blueprint

from apps.topics import handlers

blueprint = Blueprint('topic_app')
blueprint.add_route(handlers.create, '/', methods=['POST'])
blueprint.add_route(handlers.list_topics, '/', methods=['GET'])
blueprint.add_route(handlers.read, '/<id>', methods=['GET'])
blueprint.add_route(handlers.update, '/<id>', methods=['PUT'])
blueprint.add_route(handlers.delete, '/<id>', methods=['DELETE'])
