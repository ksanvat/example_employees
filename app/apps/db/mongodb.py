import logging

from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGODB_URL, MONGODB_MIN_CONNECTIONS, MONGODB_MAX_CONNECTIONS, DEV_INSERT_DATA
from .models import init_instance, deinit_instance


class DataBase:
    client: AsyncIOMotorClient = None


__db = DataBase()


async def get_database_client() -> AsyncIOMotorClient:
    return __db.client


async def get_database():
    client = await get_database_client()
    return client[MONGODB_URL.database]


async def connect_to_mongo():
    logging.info('Connecting to database...')
    __db.client = AsyncIOMotorClient(
        str(MONGODB_URL),
        minPoolSize=MONGODB_MIN_CONNECTIONS,
        maxPoolSize=MONGODB_MAX_CONNECTIONS
    )
    logging.info('Connecting to database success')

    await init_instance(await get_database())

    if DEV_INSERT_DATA:
        from apps.dev.insert_data import insert_data
        await insert_data()


async def disconnect_from_mongo():
    logging.info('Disconnecting from database...')
    __db.client.close()
    logging.info('Disconnecting from database success')

    await deinit_instance()
