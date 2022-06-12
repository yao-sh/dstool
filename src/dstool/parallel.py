from multiprocessing import cpu_count
from typing import Callable

from joblib import Parallel, delayed


def parallel(func=None,
             args=(),
             merge_func=lambda x: x,
             parallelism=cpu_count()):

    def decorator(func: Callable):

        def inner(*args, **kwargs):
            results = Parallel(n_jobs=parallelism)(
                delayed(func)(*args, **kwargs) for i in range(parallelism))
            return merge_func(results)

        return inner

    if func is None:
        # decorator was used like @parallel(...)
        return decorator
    else:
        # decorator was used like @parallel, without parens
        return decorator(func)
