from pymongo.errors import OperationFailure

from sanic.response import json
from sanic import Blueprint

from apps.news.models import News
from apps.news.repository import NewsRepo

blueprint = Blueprint('news_app')

@blueprint.route('/', methods=['POST'])
async def create(request):
    response = {}

    repo = NewsRepo(News)
    news = repo.create(**request.json)
    response = {
        'data': {
            'id': str(news.id),
            'type': 'news',
            'attributes': {
                'title': news.title,
                'content': news.content
            }
        }
    }

    return json(response)
