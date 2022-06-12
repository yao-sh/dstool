import http
import json
import os
from posixpath import join as urljoin

import requests


def push_r2(func=None):

    def inner(*args, **kwargs):
        json_data = func(*args, **kwargs)
        r2_url = os.environ.get('DSTOOL_R2_URL')
        r2_key = os.environ.get('DSTOOL_R2_KEY')
        if r2_url is not None and r2_key:
            res = requests.put(urljoin(r2_url,
                                       str(hash(str(json_data))) + ".json"),
                               data=json.dumps(json_data),
                               headers={
                                   'X-Custom-Auth-Key': r2_key,
                               })
            if res.status_code == http.HTTPStatus.OK:
                print('Pushed to R2')
            else:
                print("Failed to push to R2 : {}".format(res.text))
        else:
            print("R2 URL or key not set")

    return inner


if __name__ == "__main__":

    @push_r2
    def test():
        return {'hello': 'world'}

    test()
