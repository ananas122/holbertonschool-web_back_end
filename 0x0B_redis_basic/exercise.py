import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate random key
        key = str(uuid.uuid4())
        # Store data in Redis with random key
        self._redis.set(key, data)
        # Return the generated key
        return key
