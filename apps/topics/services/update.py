from apps.commons.services import BaseService
from apps.commons.errors import DataNotFoundError

class UpdateService(BaseService):

    _id = None 
    _repo = None
    _payload = None 

    def __init__(self, id, payload, repo):
        self._id = id 
        self._repo = repo
        self._payload = payload

    def call(self):
        try:
            doc = self._repo.findById(self._id)
            doc.update(**self._payload)

            doc.reload()
            return doc
        except DoesNotExist:
            raise DataNotFoundError('Requested id not found')
