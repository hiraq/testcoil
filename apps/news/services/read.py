from mongoengine.errors import DoesNotExist

from apps.commons.services import BaseService
from apps.commons.errors import DataNotFoundError

class ReadService(BaseService):

    _id = None 
    _repo = None 

    def __init__(self, id, repo):
        self._id = id 
        self._repo = repo

    def call(self):
        try:
            doc = self._repo.findById(self._id)
            return doc
        except DoesNotExist:
            raise DataNotFoundError('Requested id not found')
