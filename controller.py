#!coding=utf-8

from flask import make_response
import mongodb
import json
import copy
import settings


def do_good(request, resource, item_id):
    data = mongodb.service.doGoodForResource(request.args.get('good'), resource, item_id)
    return make_my_response(data)


def favourite(reuqest, resource, item_id):
    pass


def my_action(fuc, request, resource, item_id):
    return fuc(request, resource, item_id)


def make_my_response(result):
    res_data = copy.copy(settings.baseresponse)
    res_data['data'] = result['data']
    res_data['status'] = result['status']
    res_data['message'] = result['message']
    if res_data['status'] == 1:
        resp = make_response(json.dumps(res_data), 200)
    else:
        resp = make_response(json.dumps(res_data), 500)
    resp.headers['Content-Type'] = 'application/json'

    return resp
