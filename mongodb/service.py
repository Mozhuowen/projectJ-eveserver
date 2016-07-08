#!coding=utf-8

import settings
from mongodb.model import *


def result_data(data, status, message=''):
    result = dict(data=data, status=status, message=message)
    return result


def find_all_objects(model):
    return model.objects


def find_objects_by_id(model, id):
    return model.objects(id=id)


def check_email_exists(email):
    return User.objects(email=email).__len__() > 0


def increase_resource_viewcount(model, id):
    item = model.objects(id=id)[0]
    if item.view_count is None:
        item.view_count = 1
    else:
        item.view_count += 1
    try:
        item.save()
    except Exception,e:
        print Exception, e
        return 0
    print item.to_json()
    return 1


def doGoodForResource(goodaction, resource, itemid):

    item = settings.models.get(resource).objects(id=itemid)[0]
    if item.good_count is None:
        item.good_count = 1
    elif goodaction == '1':
        item.good_count += 1
    else:
        item.good_count -= 1
    try:
        item.save()
    except Exception, e:
        print Exception, e
        return result_data(0, 0, )

    return result_data(1, 1, )


def on_view_resource_item(resource, obj):
    item = find_objects_by_id(resource, obj['_id'])
    if not item.has_key('view_count'):
        item['view_count'] = 1
    else:
        item['view_count'] += 1

