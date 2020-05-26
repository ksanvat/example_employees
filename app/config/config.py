import os

import databases


def getenv_int(key, default):
    try:
        return int(os.getenv(key, default))
    except:
        return default


def getenv_bool(key, default):
    try:
        return bool(os.getenv(key, default))
    except:
        return default


def getenv_list_of_str(key, default):
    try:
        return os.getenv(key, None).split(',')
    except:
        return default


PROJECT_NAME = os.getenv('PROJECT_NAME')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', [])

MONGODB_URL = databases.DatabaseURL(
    'mongodb://{user}:{password}@{host}:{port}/{db}'.format(
        user=os.getenv('MONGODB_USER'),
        password=os.getenv('MONGODB_PASSWORD'),
        host=os.getenv('MONGODB_HOST'),
        port=os.getenv('MONGODB_PORT'),
        db=os.getenv('MONGODB_DB')
    )
)
MONGODB_MIN_CONNECTIONS = getenv_int('MONGODB_MIN_CONNECTIONS', 1)
MONGODB_MAX_CONNECTIONS = getenv_int('MONGODB_MAX_CONNECTIONS', 1)
