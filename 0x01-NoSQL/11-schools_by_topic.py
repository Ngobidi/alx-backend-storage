#!/usr/bin/env python3
'''validates module.
'''


def schools_by_topic(mongo_collection, topic):
    '''Results the list of school having a specific topic.
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
