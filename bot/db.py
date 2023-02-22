import redis

from .constant import Env

db = redis.Redis(
    host=Env.REDIS_HOST,
    port=Env.REDIS_PORT,
    password=Env.REDIS_PASSWORD,
)

db.ping()
