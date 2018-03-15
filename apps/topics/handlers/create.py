from http import HTTPStatus
from sanic.response import json

from core.helpers import jsonapi
from apps.commons.errors import DataDuplicateError
from apps.topics.models import Topic
from apps.topics.repository import TopicRepo
from apps.topics.services import CreateService

async def create(request):
    response = {}
    status = HTTPStatus.CREATED

    repo = TopicRepo(Topic)
    service = CreateService(request.json, repo)

    try:
        doc = service.call()
        response = {
            'data': {
                'id': str(doc.id),
                'type': 'topic',
                'attributes': {
                    'name': doc.name,
                }
            }
        }
    except DataDuplicateError as dup_err:
        error = jsonapi.format_error(title='Data duplication', detail=dup_err.message) 
        response = jsonapi.return_an_error(error)
        status = HTTPStatus.CONFLICT

    return json(response, status=status)
