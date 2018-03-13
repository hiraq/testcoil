from http import HTTPStatus

from mongoengine.errors import OperationError
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure

from sanic import Blueprint
from sanic.response import json

from core.helpers import jsonapi

blueprint = Blueprint('commons.exceptions')

@blueprint.exception(ServerSelectionTimeoutError)
def handle_mongo_conn(request, exception):
    error = jsonapi.format_error(title='Mongo not found', detail=str(exception))
    return json(jsonapi.return_an_error(error), status=HTTPStatus.INTERNAL_SERVER_ERROR) 

@blueprint.exception(OperationFailure)
def handle_mongo_failure(request, exception):
    error = jsonapi.format_error(title='Database failure', detail=str(exception))
    return json(jsonapi.return_an_error(error), status=HTTPStatus.INTERNAL_SERVER_ERROR) 

@blueprint.exception(OperationError)
def handle_mongo_op(request, exception):
    error = jsonapi.format_error(title='Error database operations', detail=str(exception))
    return json(jsonapi.return_an_error(error), status=HTTPStatus.INTERNAL_SERVER_ERROR) 



