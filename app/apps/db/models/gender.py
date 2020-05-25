from umongo import Document, fields


class GenderModel(Document):
    title = fields.StringField(required=True, unique=True)

    class Meta:
        collection_name = 'gender'
