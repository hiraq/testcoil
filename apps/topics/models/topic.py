from mongoengine import StringField, ListField
from apps.commons.models import BaseModel

class Topic(BaseModel):
    name = StringField(required=True)

    meta = {
        'indexes': [{
            'fields': ['name']
        }]
    }
