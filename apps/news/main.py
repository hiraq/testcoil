from sanic.response import json
from sanic import Blueprint

blueprint = Blueprint('news_app')

@blueprint.route('/', methods=['POST'])
async def create(request):
    return json({'msg': request.json.get('msg')})
