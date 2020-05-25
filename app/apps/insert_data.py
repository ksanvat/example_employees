import json

from .db.models import *


async def insert_data():
    with open('apps/data.json', 'r') as rf:
        data = json.load(rf)

    companies = {item['company'] for item in data}
    for title in companies:
        await CompanyModel(title=title).commit()

    pass

