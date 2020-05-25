import json

from apps.db.models import *


# noinspection PyTypeChecker
async def insert_data():
    with open('apps/dev/data.json', 'r') as rf:
        data = json.load(rf)

    companies = {item['company'] for item in data}
    for title in companies:
        await commit_silently(CompanyModel(title=title))

    genders = {item['gender'] for item in data}
    for title in genders:
        await commit_silently(GenderModel(title=title))

    jobs = {item['job_title'] for item in data}
    for title in jobs:
        await commit_silently(JobModel(title=title))

    for item in data:
        await commit_silently(
            EmployeeModel(
                name=item['name'],
                email=item['email'],
                age=item['age'],
                company=await CompanyModel.find_one({'title': item['company']}),
                join_date=item['join_date'],
                job=await JobModel.find_one({'title': item['job_title']}),
                gender=await GenderModel.find_one({'title': item['gender']}),
                salary=item['salary']
            )
        )


async def commit_silently(doc):
    try:
        await doc.commit()
    except:
        pass
