import json

from apps.db.models import *


async def insert_data():
    with open('apps/dev/data.json', 'r') as rf:
        data = json.load(rf)

    companies = {item['company'] for item in data}
    for title in companies:
        await CompanyModel(title=title).commit()

    genders = {item['gender'] for item in data}
    for title in genders:
        await GenderModel(title=title).commit()

    jobs = {item['job_title'] for item in data}
    for title in jobs:
        await JobModel(title=title).commit()

    for item in data:
        await EmployeeModel(
            name=item['name'],
            email=item['email'],
            age=item['age'],
            company=await CompanyModel.find_one({'title': item['company']}),
            join_date=item['join_date'],
            job=await JobModel.find_one({'title': item['job_title']}),
            gender=await GenderModel.find_one({'title': item['gender']}),
            salary=item['salary']
        ).commit()
