from fastapi import APIRouter, Depends, Query

from apps.db import get_database
from apps.crud import get_employees_with_filters, EmployeesFilterParams

router = APIRouter()


@router.get('/')
async def employees(
    offset: int = Query(0, ge=0),
    limit: int = Query(20, gt=0),
    text: str = Query(None),
    name: str = Query(None),
    age: int = Query(None, gt=0, lt=200),
    age_gt: int = Query(None, gt=0, lt=200),
    age_lt: int = Query(None, gt=0, lt=200),
    company: str = Query(None),
    job_title: str = Query(None),
    gender: str = Query(None),
    sort_by: str = Query(None),
    db=Depends(get_database)
):
    filter_params = EmployeesFilterParams(
        offset=offset,
        limit=limit,
        text=text,
        name=name,
        age=age,
        age_gt=age_gt,
        age_lt=age_lt,
        company=company,
        job_title=job_title,
        gender=gender,
        sort_by=sort_by
    )
    data = await get_employees_with_filters(db, filter_params)
    return data
