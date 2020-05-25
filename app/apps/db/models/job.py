from umongo import Document, fields

from .base import instance


# noinspection PyAbstractClass
@instance.register
class JobModel(Document):
    title = fields.StringField(required=True, unique=True)

    class Meta:
        collection_name = 'job'
