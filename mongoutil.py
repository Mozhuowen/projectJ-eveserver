#!coding=utf-8

import pymongo
import settings
from bson.objectid import ObjectId

def __init__():
    print 'init mongoutil'
    connection = pymongo.MongoClient(
        settings.MONGO_HOST,
        settings.MONGO_PORT
    )
    db = connection[settings.MONGO_DBNAME]
    """remote server need authenticate!"""
    db.authenticate(settings.MONGO_USERNAME, settings.MONGO_PASSWORD)
    print 'finished init mongoutil!'
    return db

def getMovieCollection():
    if db:
        return db[settings.MONGODB_COLLECTION_AVMOO]
    else:
        raise Exception('db is None!')

def getActressCollection():
    if db:
        return db[settings.MONGODB_COLLECTION_ACTRESS]
    else:
        raise Exception('db is None!')

def getCollection(name):
    if db:
        return db[name]
    else:
        raise Exception('db is None!')

def getUserCollection():
    if db:
        return db[settings.MONGODB_COLLECTION_USER]
    else:
        raise Exception('db is None!')

def find_movie_by_id(id):
    if not id:
        raise Exception('id is not aviable!')

    movie = getMovieCollection().find_one({'_id':ObjectId(id)})
    return movie

def find_item_by_id(resouce,id):
    if not id:
        raise Exception('id is not aviable!')

    return getCollection(resouce).find_one({'_id':ObjectId(id)})

def on_view_resource_item(resource,responseDict):
    item = find_item_by_id(resource,responseDict['_id'])
    if not item.has_key('view_count'):
        item['view_count'] = 1
    else:
        item['view_count'] = item['view_count'] + 1
    getCollection(resource).update({'_id':ObjectId(responseDict['_id'])},item,upsert=True)

def on_do_good_resource_item(resource,id):
    item = find_item_by_id(resource,id)
    if not item.has_key('good_count'):
        item['good_count'] = 1
    else:
        item['good_count'] = item['good_count'] + 1
    getCollection(resource).update({'_id':ObjectId(id)},item,upsert=True)
    return item

def on_view_movie_item(resource,responseDict):
    movie = find_movie_by_id(responseDict['_id'])
    if not movie.has_key('view_count'):
        movie['view_count'] = 1
    else:
        movie['view_count'] = movie['view_count'] +1

    getMovieCollection().update({'_id':ObjectId(responseDict['_id'])},movie,upsert=True)

db = __init__()