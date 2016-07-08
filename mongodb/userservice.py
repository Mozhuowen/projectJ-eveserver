#!coding=utf-8

from model import User
from datetime import datetime


def new_user(deviceid, userid):

    user = []
    if userid.__len__() > 0:
        user = User.objects(userid=userid)
    if user.__len__() > 0:
        user.logindate = datetime.now()
        user.deviceid = deviceid
        user.update()
        return True
    elif User.objects(deviceid=deviceid).__len__() > 0:
        user = User.objects(deviceid=deviceid)[0]
        user.logindate = datetime.now()
        user.update
    else:
        user = User(userid=userid, deviceid=deviceid, device_ids=[deviceid, ], createdate=datetime.now(), logindate=datetime.now())
        user.save()
        return True
