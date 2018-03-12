import datetime
from mongoengine import Document, DateTimeField

class BaseModel(Document):
    created_at = DateTimeField()
    updated_at = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'abstract': True}
