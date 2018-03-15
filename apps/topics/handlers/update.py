import datetime
from http import HTTPStatus
from sanic.response import json

from core.helpers import jsonapi
from apps.commons.errors import DataNotFoundError

from apps.topics.models import Topic
from apps.topics.repository import TopicRepo
from apps.topics.services import UpdateService 

async def update(request, id):
    response = {}
    status = HTTPStatus.OK

    repo = TopicRepo(Topic)
    service = UpdateService(id, request.json, repo)

    try:
        doc = service.call()
        response = {
            'data': {
                'id': str(doc.id),
                'type': 'topic',
                'attributes': {
                    'name': doc.name,
                    'updated_at': str(doc.updated_at) 
                }
            }
        }
    except DataNotFoundError as not_found_err:
        error = jsonapi.format_error(title='Data not found', detail=not_found_err.message) 
        response = jsonapi.return_an_error(error)
        status = HTTPStatus.NOT_FOUND

    return json(response, status=status)
