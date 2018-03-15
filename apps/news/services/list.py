from mongoengine.errors import DoesNotExist

from apps.commons.services import BaseService
from apps.commons.errors import DataNotFoundError

class ListService(BaseService):

    def __init__(self, repo, topicRepo, limit=0, skip=0, status=None, order_by='-created_at', topics=None):
        self._repo = repo
        self._limit = limit
        self._skip = skip
        self._status = status
        self._order_by = order_by
        self._topics = topics
        self._topicRepo = topicRepo

    def call(self):
        docs = []
        if self._status is None:
            docs = self._repo.getAll()
        else:
            if self._topics is not None:
                if self._topics.find(',') >= 1:
                    topics = self._topics.split(',')
                else:
                    topics = [self._topics]

                def _find_topics(topic):
                    doc = self._topicRepo.findBy(name=topic)
                    return doc.first()

                topics = list(map(_find_topics, topics))
                docs = self._repo.findBy(publish_status=self._status, topics__all=topics)
            else:
                docs = self._repo.findBy(publish_status=self._status)

        limit = int(self._limit)
        skip = int(self._skip)

        if limit >= 1:
            docs = docs.limit(int(self._limit))

        if skip >= 1:
            docs = docs.skip(int(self._skip))

        if self._order_by is not None:
            docs = docs.order_by(self._order_by)

        return docs
