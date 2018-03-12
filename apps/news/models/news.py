from mongoengine import StringField, ListField
from apps.commons.models import BaseModel

class News(BaseModel):
    title = StringField(required=True)
    content = StringField(required=True)
    tags = ListField(StringField())

    meta = {
        'indexes': ['$title', '#title', '$content']
    }
