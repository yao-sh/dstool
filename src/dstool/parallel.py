from multiprocessing import cpu_count
from typing import Callable

from joblib import Parallel, delayed

def chunks(lst, n):
    """Yields successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def parallel(func=None,
             args=(),
             merge_func=lambda x: x,
             parallelism=cpu_count()):
    """Allocates tasks to multiple cores, by default it uses cpu_count() cores."""
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
