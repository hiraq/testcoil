from bson.objectid import ObjectId
from apps.commons.repositories import BaseRepository

class CommonMongoRepo(BaseRepository):

    def create(self, **kwargs):
        doc = self._model(**kwargs)
        doc.save()
        return doc

    def edit(self, id, **kwargs):
        doc = self._model.objects(id=id)
        doc.update(**kwargs)
        return doc

    def delete(self, id, options=None):
        doc = self._model.objects(id=id)
        doc.delete()

    def findById(self, id):
        doc = self._model.objects.get(id=ObjectId(id))
        return doc

    def findBy(self, **kwargs):
        doc = self._model.objects(**kwargs)
        return doc

