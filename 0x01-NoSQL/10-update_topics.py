#!/usr/bin/env python3
'''module.'''


def update_topics(mongo_collection, name, topics):
    '''Change all topics of a collection document based on the name.
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
