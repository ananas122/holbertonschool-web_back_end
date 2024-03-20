#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union


class Cache:
    """Writing strings to Redis """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store """
        # Generate random key
        key = str(uuid.uuid4())
        # Store data in Redis with random key
        self._redis.set(key, data)
        # Return the generated key
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        key = self._redis.get(key)
        if fn:
            return fn(key)

    def get_str(self, key: str):
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str):
        return self.get(key, fn=int)


# Test the Cache class
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
