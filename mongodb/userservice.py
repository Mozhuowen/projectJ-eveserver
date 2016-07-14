#!coding=utf-8

from model import User
from datetime import datetime
from util import str_util


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


def login(userid='', deviceid='', email='', passwd=''):

    user = []
    if userid.__len__() == 0:
        user = new_user(deviceid, userid)
        user.email = email
        user.passwd = passwd
        user.haslogin = 1
        user.save()
    elif not check_hasemail(email=email):
        return {}, 0, 'email 不存在'
    elif not check_passwd(email=email, passwd=passwd):
        return {}, 0, '密码不正确'
    else:
        user = User.objects(email=email)[0]
        user.logindate = datetime.now()
        user.haslogin = 1
        user.save()
    return user.to_mongo(), 1, ''


def regist(userid='', deviceid='', email='', passwd=''):

    user = []
    if userid.__len__() == 0:
        user = new_user(deviceid, userid)
        user.email = email
        user.passwd = passwd
        user.nick_name = str_util.get_random_string(8)
        user.haslogin = 1
        user.save()
    elif check_hasemail(email):
        return {}, 0, '该email已经存在'
    else:
        user = User.objects(id=userid)[0]
        user.email = email
        user.passwd = passwd
        user.nick_name = str_util.get_random_string(8)
        user.haslogin = 1
        user.save()
    return user.to_mongo(), 1, ''


def check_hasemail(email=''):
    user = User.objects(email=email)
    return user.__len__() > 0

def check_passwd(email='', passwd=''):
    user = User.objects(email=email)[0]
    return user.passwd == passwd