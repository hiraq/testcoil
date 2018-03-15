from http import HTTPStatus
from sanic.response import json

from core.helpers import jsonapi
from apps.commons.errors import DataNotFoundError

from apps.news.models import News
from apps.news.repository import NewsRepo
from apps.news.services import ListService 

from apps.topics.models import Topic
from apps.topics.repository import TopicRepo

async def list_news(request):
    status = HTTPStatus.OK
    args = request.raw_args

    repo = NewsRepo(News)
    topicRepo = TopicRepo(Topic)

    service = ListService(
        repo, 
        topicRepo,
        limit=args.get('limit', 0), 
        skip=args.get('skip', 0), 
        status=args.get('status', 'published'),
        order_by=args.get('order_by'),
        topics=args.get('topics')
    )

    docs = service.call()
    def _mapper(data):
        return {
            'type': 'news',
            'id': str(data.id),
            'attributes': {
                'title': data.title,
                'content': data.content,
                'topics': list(map(lambda topic: topic.name, data.topics)),
                'created_at': str(data.created_at),
                'updated_at': str(data.updated_at)
            }
        }

    response = {
        'meta': {
            'total-data': docs.count(),
            'limit': args.get('limit'),
            'skip': args.get('skip'),
            'order': args.get('order_by'),
            'topics': args.get('topics')
        },
        'data': list(map(_mapper, docs))
    }

    return json(response, status=status)

