# -*- coding: utf-8 -*-

from datetime import datetime
from model import Share, Simplemovie, Avmoo, User
import userservice
import movieservice
from util import JJQuerySet


def create_share(userid='', content='', movie_code=''):
    if not userservice.check_user_exist(userid=userid):
        return {}, 0, 'user not exist!'

    if not movieservice.check_movie_exist(movie_code=movie_code):
         return {}, 0, 'movie not exist!'

    movie = Avmoo.objects(code=movie_code)[0]
    simple_movie = Simplemovie(movie_code=movie.code,
                               cover_image=movie.image_small_url,
                               actress=movie.actress[0]['name'])
    share = Share(userid=userid, content=content, movie=simple_movie, time=datetime.now())
    share.save()
    return {
               'status': 1
           }, 1, ''


def get_sharelist(page=1):
    shares = Share.objects.order_by('-update_time')
    if shares.__len__() == 0:
        return {}, 1, ''

    per_page = 26
    shares = shares[(page-1) * per_page:(page * per_page)-1]
    shares = getreturn_sharelist(shares)
    return shares, 1, ''


def getreturn_sharelist(shares):
    data = []
    for s in shares:
        user = User.objects(id=s.userid)[0]
        s.nick_name = user.nick_name
        s.avater = user.avater
        data.append(s.to_mongo())
    return data
