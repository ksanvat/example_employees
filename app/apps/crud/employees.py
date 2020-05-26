import re

from apps.db.models import EmployeeModel


class EmployeesFilterParams:
    def __init__(
        self,
        offset,
        limit,
        text,
        name,
        age,
        age_gt,
        age_lt,
        company,
        job_title,
        gender
    ):
        self.offset = offset
        self.limit = limit
        self.text = text
        self.name = name
        self.age = age
        self.age_gt = age_gt
        self.age_lt = age_lt
        self.company = company
        self.job_title = job_title
        self.gender = gender


async def get_employees_with_filters(db, filter_params):
    params = {}

    if filter_params.text is not None:
        params['$text'] = {'$search': filter_params.text}

    if filter_params.name is not None:
        params['name_lower'] = re.compile(filter_params.name.lower())

    if filter_params.age is not None:
        params['age'] = filter_params.age
    else:
        if filter_params.age_gt is not None:
            params.setdefault('age', {}).update({'$gt': filter_params.age_gt})

        if filter_params.age_lt is not None:
            params.setdefault('age', {}).update({'$lt': filter_params.age_lt})

    if filter_params.company is not None:
        params['company_lower'] = filter_params.company.lower()

    if filter_params.job_title is not None:
        params['job_title_lower'] = filter_params.job_title.lower()

    if filter_params.gender is not None:
        params['gender'] = filter_params.gender.lower()

    cursor = db.employee.find(
        params,
        skip=filter_params.offset,
        limit=filter_params.limit
    ).sort([
        ('date_join', -1)
    ])

    data = []
    async for row in cursor:
        data.append(EmployeeModel.serialize(row))

    return data
