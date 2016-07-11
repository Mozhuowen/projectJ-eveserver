#!coding=utf-8

from model import User
from datetime import datetime


def new_user(deviceid, userid):

    user = []
    if userid.__len__() > 0:
        user = User.objects(id=userid)
    if user.__len__() > 0:
        user = user[0]
        user.logindate = datetime.now()
        user.deviceid = deviceid
        user.save()
    # elif User.objects(deviceid=deviceid).__len__() > 0:
    #     user = User.objects(deviceid=deviceid)[0]
    #     user.logindate = datetime.now()
    #     user.update
    else:
        user = User(deviceid=deviceid, device_ids=[deviceid, ], createdate=datetime.now(), haslogin=0)
        user.save()
    return user
