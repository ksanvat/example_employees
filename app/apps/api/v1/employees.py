from fastapi import APIRouter, Depends

from apps.db import get_database

router = APIRouter()


@router.get('/')
async def employees(
    db=Depends(get_database)
):
    data = []
    cursor = db.employee.find().sort([('date_join', -1)])

    for row in await cursor.to_list(length=10):
        data.append(row)

    # async for row in db.employee.find():
    #     data.append(row['salary'])

    return data
