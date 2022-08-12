import pycouchdb
import os
from loguru import logger
from datetime import datetime

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


def add_event(payload, tags, previous_timestamp=None):
    dt = datetime.now()
    timestamp = datetime.timestamp(dt)
    json_data = {
        "timestamp": timestamp,
        "payload": payload,
        "tags": tags,
        
    }
    if previous_timestamp is not None:
        json_data['previous'] = previous_timestamp
        dt_obj = datetime.fromtimestamp(previous_timestamp)
        json_data['duration'] = (dt - dt_obj).total_seconds()
    couchdb_connection = os.environ.get('DSTOOL_COUCHDB_URL')
    couchdb_database = 'time_series'
    server = pycouchdb.Server(couchdb_connection)
    db = server.database(couchdb_database)
    doc = db.save(json_data)
    logger.info("Pushed to CouchDB: {}".format(doc))
    return timestamp


if __name__ == "__main__":

    # @push_couch
    # def test():
    #     return {'hello': 'world'}
    # test()
    import timeit
    ts = add_event({"test_payload": "test"}, ["test"])
    add_event({"test_payload": "test"}, ["test"], ts)