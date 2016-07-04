#!coding=utf-8

from mongodb import service
from settings import models

def pre_GET(resource, request, lookup):
    pass
    # print 'pre_GET'
    # print resource
    # print request
    # print lookup


def on_fetched_item(resource_name, response):
    # mongoutil.on_view_resource_item(resource_name,response)
    service.increase_resource_viewcount(models.get(resource_name), response['_id'])
    print 'finished on_fetched_item!'


def post_get_callback(resource, request, response):
    try:
        print resource
        print request.headers
        print request.headers['deviceid']
        print response
    except Exception,e:
        print Exception,':', e