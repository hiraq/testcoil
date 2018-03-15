from http import HTTPStatus
from sanic.response import json

from core.helpers import jsonapi
from apps.commons.errors import DataNotFoundError

from apps.news.models import News
from apps.news.repository import NewsRepo
from apps.news.services import ReadService 

async def read(request, id):
    response = {}
    status = HTTPStatus.OK

    repo = NewsRepo(News)
    service = ReadService(id, repo)

    try:
        doc = service.call()
        response = {
            'data': {
                'id': str(doc.id),
                'type': 'news',
                'attributes': {
                    'title': doc.title,
                    'content': doc.content,
                    'topics': list(map(lambda topic: topic.name, doc.topics)),
                    'created_at': str(doc.created_at),
                    'updated_at': str(doc.updated_at)
                }
            }
        }
    except DataNotFoundError as not_found_err:
        error = jsonapi.format_error(title='Data not found', detail=not_found_err.message) 
        response = jsonapi.return_an_error(error)
        status = HTTPStatus.NOT_FOUND

    return json(response, status=status)
