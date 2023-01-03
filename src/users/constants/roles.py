from enum import Enum
from functools import lru_cache

__all__ = ["Role"]


class Role(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"

    @classmethod
    @lru_cache
    def values(cls):
        results = []
        for element in cls:
            el = (element.value, element.value.capitalize())
            results.append(el)
        return results
