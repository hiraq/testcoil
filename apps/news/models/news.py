from mongoengine import StringField, ListField
from apps.commons.models import BaseModel

class News(BaseModel):
    PUBLISH_STATUS = ('draft', 'published', 'archived')

    title = StringField(required=True)
    content = StringField(required=True)
    tags = ListField(StringField())
    publish_status = StringField(choices=PUBLISH_STATUS, default='published')

    meta = {
        'indexes': [{
            'fields': ['$title', '$content']
        }]
    }
