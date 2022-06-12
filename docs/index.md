# DSTool

> Toolkit for Data Scientists


***Credits***: Derived from https://bytepawn.com/python-decorators-for-data-scientists.html#python-decorators-for-data-scientists

## Usage

```
from dstool.storage import push_r2
@push_r2
def f(x):
    return {"result": 0}
```

Requires `DSTOOL_R2_URL` and `DSTOOL_R2_KEY` to be set in the environment.`

```

```