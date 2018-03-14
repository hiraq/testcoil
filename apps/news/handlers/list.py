from http import HTTPStatus
from sanic.response import json

from core.helpers import jsonapi
from apps.commons.errors import DataNotFoundError

from apps.news.models import News
from apps.news.repository import NewsRepo
from apps.news.services import ListService 

async def list_news(request):
    status = HTTPStatus.OK
    args = request.raw_args

    repo = NewsRepo(News)
    service = ListService(
        repo, 
        limit=args.get('limit', 0), 
        skip=args.get('skip', 0), 
        status=args.get('status'),
        order_by=args.get('order_by')
    )

    docs = service.call()
    def _mapper(data):
        return {
            'type': 'news',
            'id': str(data.id),
            'attributes': {
                'title': data.title,
                'content': data.content,
                'created_at': str(data.created_at),
                'updated_at': str(data.updated_at)
            }
        }

    response = {
        'meta': {
            'total-data': docs.count(),
            'limit': args.get('limit'),
            'skip': args.get('skip'),
            'order': args.get('order_by')
        },
        'data': list(map(_mapper, docs))
    }

    return json(response, status=status)

