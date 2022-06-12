from timeit import default_timer
from typing import Callable


def measure(func: Callable):

    def inner(*args, **kwargs):
        start = default_timer()
        func(*args, **kwargs)
        elapsed_sec = default_timer - start
        print(f'Elapsed: {elapsed_sec:.3f} secs')

    return inner
