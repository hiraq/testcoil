from mongoengine import StringField, ListField, ReferenceField, PULL
from apps.commons.models import BaseModel
from apps.topics.models import Topic

class News(BaseModel):
    PUBLISH_STATUS = ('draft', 'published', 'archived')

    title = StringField(required=True)
    content = StringField(required=True)
    topics = ListField(ReferenceField(Topic, reverse_delete_rule=PULL))
    publish_status = StringField(choices=PUBLISH_STATUS, default='published')

    meta = {
        'indexes': [{
            'fields': ['$title', '$content']
        }]
    }
