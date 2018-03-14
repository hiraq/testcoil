from http import HTTPStatus
from sanic.response import json

from core.helpers import jsonapi
from apps.commons.errors import DataNotFoundError

from apps.news.models import News
from apps.news.repository import NewsRepo
from apps.news.services import DeleteService 

async def delete(request, id):
    response = {}
    status = HTTPStatus.OK

    repo = NewsRepo(News)
    service = DeleteService(id, repo)

    try:
        service.call()
        response['data'] = None
    except DataNotFoundError as not_found_err:
        error = jsonapi.format_error(title='Data not found', detail=not_found_err.message) 
        response = jsonapi.return_an_error(error)
        status = HTTPStatus.NOT_FOUND

    return json(response, status=status)
