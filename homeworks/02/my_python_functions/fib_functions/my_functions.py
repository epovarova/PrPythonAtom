from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n > -1:
        return True
    raise Exception("Error")
