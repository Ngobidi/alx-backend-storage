#!/usr/bin/env python3
'''validates module.
'''


def list_all(mongo_collection):
    '''displays all documents in a collections.
    '''
    return [doc for doc in mongo_collection.find()]
