from multiprocessing import cpu_count
from typing import Callable
from joblib import parallel_backend, Parallel, delayed, effective_n_jobs
from sklearn.utils import gen_even_slices
from sklearn.utils.validation import _num_samples

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

def parallel_apply(df, func, n_jobs= -1, **kwargs):
    """ Pandas apply in parallel using joblib. 
    Uses sklearn.utils to partition input evenly.
    
    Args:
        df: Pandas DataFrame, Series, or any other object that supports slicing and apply.
        func: Callable to apply
        n_jobs: Desired number of workers. Default value -1 means use all available cores.
        **kwargs: Any additional parameters will be supplied to the apply function
        
    Returns:
        Same as for normal Pandas DataFrame.apply()
        
    """
    
    if effective_n_jobs(n_jobs) == 1:
        return df.apply(func, **kwargs)
    else:
        ret = Parallel(n_jobs=n_jobs)(
            delayed(type(df).apply)(df[s], func, **kwargs)
            for s in gen_even_slices(_num_samples(df), effective_n_jobs(n_jobs)))
        return pd.concat(ret)
