import datetime
from http import HTTPStatus
from sanic.response import json

from core.helpers import jsonapi
from apps.commons.errors import DataNotFoundError

from apps.news.models import News
from apps.news.repository import NewsRepo
from apps.news.services import UpdateService 

async def update(request, id):
    response = {}
    status = HTTPStatus.OK

    repo = NewsRepo(News)
    service = UpdateService(id, request.json, repo)

    try:
        news = service.call()
        response = {
            'data': {
                'id': str(news.id),
                'type': 'news',
                'attributes': {
                    'title': news.title,
                    'content': news.content,
                    'updated_at': str(news.updated_at) 
                }
            }
        }
    except DataNotFoundError as not_found_err:
        error = jsonapi.format_error(title='Data not found', detail=not_found_err.message) 
        response = jsonapi.return_an_error(error)
        status = HTTPStatus.NOT_FOUND

    return json(response, status=status)
