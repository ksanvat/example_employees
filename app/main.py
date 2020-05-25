from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from apps.db import connect_to_mongo, disconnect_from_mongo
from config import PROJECT_NAME, ALLOWED_HOSTS
from apps.api import router as api_router

# from .core.errors import http_422_error_handler, http_error_handler


app = FastAPI(title=PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler('startup', connect_to_mongo)
app.add_event_handler('shutdown', disconnect_from_mongo)

# app.add_exception_handler(HTTPException, http_error_handler)
# app.add_exception_handler(HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)

app.include_router(api_router, prefix='/api')
