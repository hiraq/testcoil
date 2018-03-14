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
        is_name_duplicate = self._check_name_duplicate(self._payload.get('name'))
        if is_name_duplicate:
            raise DataDuplicateError('Name has been exist')

        self._payload['created_at'] = datetime.datetime.utcnow()
        doc = self._repo.create(**self._payload)
        return doc

    def _check_name_duplicate(self, name):
        names = self._repo.findBy(name=name)
        return names.count() > 0
