import datetime

from apps.commons.services import BaseService
from apps.commons.errors import DataDuplicateError

class CreateService(BaseService):
    
    _repo = None 
    _payload = {}

    def __init__(self, payload, repo):
        self._payload = payload
        self._repo = repo

    def call(self):
        is_title_duplicate = self._check_title_duplicate(self._payload.get('title'))
        if is_title_duplicate:
            raise DataDuplicateError('Title has been exist')

        self._payload['created_at'] = datetime.datetime.utcnow()
        doc = self._repo.create(**self._payload)
        return doc

    def _check_title_duplicate(self, title):
        title = self._repo.findBy(title=title)
        return title.count() > 0
