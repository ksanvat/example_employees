from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import PROJECT_NAME, ALLOWED_HOSTS
from apps.db import connect_to_mongo, disconnect_from_mongo
from apps.api import router as api_router


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

app.include_router(api_router, prefix='/api')
