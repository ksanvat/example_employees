from umongo import Document, fields

from .base import instance


@instance.register
class GenderModel(Document):
    title = fields.StringField(required=True, unique=True)

    class Meta:
        collection_name = 'gender'
