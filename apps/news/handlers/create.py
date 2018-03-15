from http import HTTPStatus
from sanic.response import json

from core.helpers import jsonapi
from apps.commons.errors import DataDuplicateError
from apps.news.models import News
from apps.news.repository import NewsRepo
from apps.news.services import CreateService

from apps.topics.models import Topic
from apps.topics.repository import TopicRepo

async def create(request):
    response = {}
    status = HTTPStatus.CREATED

    repo = NewsRepo(News)
    topicRepo = TopicRepo(Topic)
    service = CreateService(request.json, repo, topicRepo)

    try:
        news = service.call()
        response = {
            'data': {
                'id': str(news.id),
                'type': 'news',
                'attributes': {
                    'title': news.title,
                    'content': news.content,
                    'topics': list(map(lambda topic: topic.name, news.topics))
                }
            }
        }
    except DataDuplicateError as dup_err:
        error = jsonapi.format_error(title='Data duplication', detail=dup_err.message) 
        response = jsonapi.return_an_error(error)
        status = HTTPStatus.CONFLICT

    return json(response, status=status)
