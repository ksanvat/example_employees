import logging

from motor.motor_asyncio import AsyncIOMotorClient
from umongo import MotorAsyncIOInstance

from config import MONGODB_URL, MONGODB_MIN_CONNECTIONS, MONGODB_MAX_CONNECTIONS


class DataBase:
    client = None


class Instance(MotorAsyncIOInstance):
    async def init(self, db):
        super().init(db=db)

        for doc in self._doc_lookup.values():
            await doc.ensure_indexes()

    async def deinit(self):
        self._db = None


__db = DataBase()
instance = Instance()


async def get_database_client():
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

    await instance.init(await get_database())


async def disconnect_from_mongo():
    logging.info('Disconnecting from database...')
    __db.client.close()
    logging.info('Disconnecting from database success')

    await instance.deinit()
