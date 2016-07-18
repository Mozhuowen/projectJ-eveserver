#!coding=utf-8

from flask import make_response, send_file
from bson import json_util
from util import json_util_jj,helper
import mongodb
from mongodb import userservice, model, fileservice
import copy
import settings


def do_good(request, resource, item_id):
    data = mongodb.service.doGoodForResource(request.args.get('good'), resource, item_id)
    return make_my_response(data)


def favourite(reuqest, resource, item_id):
    pass


def create_user(request):
    pass


def new_user(request):
    deviceid = ''
    userid = ''
    try:
        deviceid = request.headers['DeviceId']
        userid = request.headers['UserId']
    except Exception, e:
        return make_my_response(result_data(0, 0,), status_code=500)

    result = userservice.new_user(deviceid, userid)
    return make_my_response(result_data(result.to_mongo(), 1,))


def login(request):
    try:
        userid = request.headers['UserId']
        deviceid = request.headers['DeviceId']
        email = request.args.get('email')
        passwd = request.args.get('passwd')
    except Exception, e:
        return make_my_response(result_data(0, 0,), status_code=500)

    result, status_code, message = userservice.login(userid=userid, deviceid=deviceid, email=email, passwd=passwd)
    return make_my_response(result_data(result, status_code, message))


def regist(request):
    try:
        userid = request.headers['UserId']
        deviceid = request.headers['DeviceId']
        email = request.args.get('email')
        passwd = request.args.get('passwd')
    except Exception, e:
        return make_my_response(result_data(0, 0, ), status_code=500)

    result, status_code, message = userservice.regist(userid=userid, deviceid=deviceid, email=email, passwd=passwd)
    return make_my_response(result_data(result, status_code, message))


def change_username(request):
    pass


def change_nickname(request):
    pass


def change_avater(request):
    try:
        userid = request.headers['UserId']
        deviceid = request.headers['DeviceId']
        image = request.args.get('image')
    except Exception, e:
        return make_my_response(result_data(0, 0, ), status_code=500)


def upload_avater(request):
    result, status_code, message = fileservice.save_upload_file(request)
    return make_my_response(result_data(result, status_code, message))


def get_file(filename):
    return send_file('/usr/local/python/projectJ-eveserver/static/'+filename)


def my_action(fuc, request, resource, item_id):
    return fuc(request, resource, item_id)


def user_action(fuc, request):
    return fuc(request)


# test function
def test_method(id):
    # data = mongodb.service.find_all_objects(settings.models.get('movies'))[:3]
    data = model.User.objects()
    result = result_data(data.to_mongo(), 1, )
    return make_my_response(result)


def result_data(data, status, message=''):
    result = dict(data=data, status=status, message=message)
    return result


def make_my_response(result, status_code=200):
    res_data = copy.copy(settings.baseresponse)
    res_data['data'] = result['data']
    res_data['status'] = result['status']
    res_data['message'] = result['message']
    resp = make_response(json_util_jj.dumps(res_data), status_code)
    resp.headers['Content-Type'] = 'application/json'

    return resp
