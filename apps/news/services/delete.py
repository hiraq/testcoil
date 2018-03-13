from mongoengine.errors import DoesNotExist, MultipleObjectsReturned

from apps.commons.services import BaseService
from apps.commons.errors import DataNotFoundError

class DeleteService(BaseService):

    _id = None 
    _repo = None 

    def __init__(self, id, repo):
        self._id = id 
        self._repo = repo

    def call(self):
        try:
            objects = self._repo.findBy(id=self._id)
            doc = objects.get()
            doc.delete()
        except DoesNotExist:
            raise DataNotFoundError('Requested id not found')
