# -*- coding: utf-8 -*-

"""
    eve-demo settings
    ~~~~~~~~~~~~~~~~~

    Settings file for our little demo.

    PLEASE NOTE: We don't need to create the two collections in MongoDB.
    Actually, we don't even need to create the database: GET requests on an
    empty/non-existant DB will be served correctly ('200' OK with an empty
    collection); DELETE/PATCH will receive appropriate responses ('404' Not
    Found), and POST requests will create database and collections when needed.
    Keep in mind however that such an auto-managed database will most likely
    perform poorly since it lacks any sort of optimized index.

    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_HOST = '45.33.41.182'
MONGO_PORT = 27017
MONGO_USERNAME = 'avmoo'
MONGO_PASSWORD = '0603'
MONGO_DBNAME = 'stackoverflow'
MONGODB_COLLECTION_AVMOO = 'avmoo'
MONGODB_COLLECTION_ACTRESS = "actress"
MONGODB_COLLECTION_USER = "user"


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET','POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

SOFT_DELETE = True
SORTING = True
# Our API will expose two resources (MongoDB collections): 'people' and
# 'works'. In order to allow for proper data validation, we define beaviour
# and structure.
people = {
    # 'title' tag used in item links.
    'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/people/<lastname>/'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'firstname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'lastname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'required': True,
            # talk about hard constraints! For the purpose of the demo
            # 'lastname' is an API entry-point, so we need it to be unique.
            'unique': True,
        },
        # 'role' is a list, and can only contain values from 'allowed'.
        'role': {
            'type': 'list',
            'allowed': ["author", "contributor", "copy"],
        },
        # An embedded 'strongly-typed' dictionary.
        'location': {
            'type': 'dict',
            'schema': {
                'address': {'type': 'string'},
                'city': {'type': 'string'}
            },
        },
        'born': {
            'type': 'datetime',
        },
    }
}

works = {
    # if 'item_title' is not provided Eve will just strip the final
    # 's' from resource name, and use it as the item_title.
    #'item_title': 'work',

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': {
        'title': {
            'type': 'string',
            'required': True,
        },
        'description': {
            'type': 'string',
        },
        'owner': {
            'type': 'objectid',
            'required': True,
            # referential integrity constraint: value must exist in the
            # 'people' collection. Since we aren't declaring a 'field' key,
            # will default to `people._id` (or, more precisely, to whatever
            # ID_FIELD value is).
            'data_relation': {
                'resource': 'people',
                # make the owner embeddable with ?embedded={"owner":1}
                'embeddable': True
            },
        },
    }
}

question = {
    'schema': {
        'title': {
            'type':'string',
            'required':True,
        },
        'url': {
            'type': 'string',
            'required':True,
        },
    }
}

movies = {

    'allow_unknown': True,

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'title'
    },

    'schema': {
        'title': {
            'type': 'string',
            'required': True,
        },
        'url_detail': {
            'type': 'string',
        },
        'desc': {
            'type': 'string',
        },
        'firstname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'lastname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            # talk about hard constraints! For the purpose of the demo
            # 'lastname' is an API entry-point, so we need it to be unique.
            'unique': True,
        },
        'image_urls': {
            'type': 'list',
        },
        'images': {
            'type':'list',
        }
    }
}

avmoo = {

    'schema': {
        'code': {
            'type': 'string',
            'required': True,
        },
        'title': {
            'type': 'string',
            'required': True,
        },
        'publishtime': {
            'type':'string',
            'required': True,
        },
        'length': {
            'type': 'string',
            'required': True,
        },
        'image_large_url': {
            'type': 'string',
            'required': True,
        },
        'image_small_url': {
            'type': 'string',
            'required': True,
        },
        'actress': {
            'type':'list'
        },
        'sample_images': {
            'type': 'list'
        }
    }
}

actress = {

    'schema': {
        'actressname': {
            'type': 'string',
            'required': True,
        },
        'url_movies': {
            'type': 'string',
            'required': True,
        },
        'image_urls': {
            'type': 'list',
            'required': True,
        },
        'actresscode': {
            'type': 'string',
            'required': True,
        },
        'image_cover_url': {
            'type': 'string',
            'required': True,
        }
    }
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'people': people,
    'works': works,
    'question':question,
    'movies': movies,
    'avmoo': avmoo,
    'actress': actress,
}
