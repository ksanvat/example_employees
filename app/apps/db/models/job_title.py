from umongo import Document, fields


class JobTitleModel(Document):
    title = fields.StringField(required=True, unique=True)

    class Meta:
        collection_name = 'job_title'
