import datetime

from apps.commons.services import BaseService
from apps.commons.errors import DataDuplicateError

class CreateService(BaseService):
    
    def __init__(self, payload, repo, topicRepo):
        self._payload = payload
        self._repo = repo
        self._topicRepo = topicRepo

    def call(self):
        is_title_duplicate = self._check_title_duplicate(self._payload.get('title'))
        if is_title_duplicate:
            raise DataDuplicateError('Title has been exist')

        if self._payload.get('topics') is not None:
            self._payload['topics'] = self._save_topics(self._payload.get('topics'))

        self._payload['created_at'] = datetime.datetime.utcnow()
        doc = self._repo.create(**self._payload)
        return doc

    def _check_title_duplicate(self, title):
        title = self._repo.findBy(title=title)
        return title.count() > 0

    def _save_topics(self, topics):
        topics_created = []
        if len(topics) >= 1:
            for topic in topics:
                topic_exist = self._topicRepo.findBy(name=topic)
                if topic_exist.count() < 1:
                    doc = self._topicRepo.create(name=topic)

                topics_created.append(topic_exist.get())

        return topics_created
