from umongo import Document, fields

from .base import instance
from .company import CompanyModel
from .job_title import JobTitleModel
from .gender import GenderModel


@instance.register
class EmployeeModel(Document):
    name = fields.StringField(required=True)
    email = fields.EmailField(required=True)
    age = fields.IntegerField(required=True)
    company = fields.ReferenceField(document=CompanyModel, required=True)
    join_date = fields.DateTimeField(required=True)
    job_title = fields.ReferenceField(document=JobTitleModel, required=True)
    gender = fields.ReferenceField(document=GenderModel, required=True)
    salary = fields.IntegerField(required=True)

    class Meta:
        collection_name = 'employee'
