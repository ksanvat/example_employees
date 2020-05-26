import asyncio
import json

from apps.db import connect_to_mongo, disconnect_from_mongo
from apps.db.models import EmployeeModel


# noinspection PyTypeChecker
async def insert_data():
    await connect_to_mongo()

    with open('fixtures/data.json', 'r') as rf:
        data = json.load(rf)

    async for doc in EmployeeModel.find():
        await doc.remove()

    for item in data:
        await commit_silently(
            EmployeeModel,
            name=item['name'],
            name_lower=item['name'].lower(),
            email=item['email'],
            age=item['age'],
            company=item['company'],
            company_lower=item['company'].lower(),
            join_date=item['join_date'],
            job_title=item['job_title'],
            job_title_lower=item['job_title'].lower(),
            gender=item['gender'].lower(),
            salary=item['salary'],
        )

    await disconnect_from_mongo()


async def commit_silently(model, **kwargs):
    try:
        await model(**kwargs).commit()
    except Exception as e:
        raise e


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(insert_data())
