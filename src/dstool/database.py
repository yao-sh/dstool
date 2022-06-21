import pycouchdb
import http
import json
import os
from posixpath import join as urljoin
from loguru import logger
import requests

def push_couch(func=None):

    def inner(*args, **kwargs):
        json_data = func(*args, **kwargs)
        couchdb_connection = os.environ.get('DSTOOL_COUCHDB_URL')
        couchdb_database = os.environ.get('DSTOOL_COUCHDB_DATABASE')
        server = pycouchdb.Server(couchdb_connection)
        db = server.database(couchdb_database)
        doc = db.save(json_data)
        logger.info("Pushed to CouchDB: {}".format(doc))
    return inner


if __name__ == "__main__":

    @push_couch
    def test():
        return {'hello': 'world'}
    test()
