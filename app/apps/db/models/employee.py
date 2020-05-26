from umongo import Document, fields

from . import instance


# noinspection PyAbstractClass
@instance.register
class EmployeeModel(Document):
    name = fields.StringField(required=True)
    name_lower = fields.StringField(required=True)
    email = fields.EmailField(required=True)
    age = fields.IntegerField(required=True)
    company = fields.StringField(required=True)
    company_lower = fields.StringField(required=True)
    join_date = fields.DateTimeField(required=True)
    job_title = fields.StringField(required=True)
    job_title_lower = fields.StringField(required=True)
    gender = fields.StringField(required=True)
    salary = fields.IntegerField(required=True)

    class Meta:
        collection_name = 'employee'
        indexes = (('$name', '$company', '$job_title'),)

    @classmethod
    def serialize(cls, dct):
        return {key: value for key, value in dct.items() if key != '_id' and not key.endswith('_lower')}
