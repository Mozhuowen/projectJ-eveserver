# -*- coding: utf-8 -*-

from model import Like, Avmoo
from datetime import datetime
from util import str_util
import userservice


def like_movie(userid='', movie_code=''):
    if not userservice.check_user_exist(userid=userid):
        return {}, 0, '用户不存在'

    if not check_movie_exist(movie_code=movie_code):
        return {}, 0, '影片不存在'

    movie = Avmoo.objects(code=movie_code)[0]
    like = Like(userid=userid, movie_code=movie.code, movieid=movie.id)
    like.save()

    if movie.view_count is None:
        movie.view_count = 1
    else:
        movie.view_count += 1
    movie.save()
    return {}, 1, ''


def check_movie_exist(movie_code=''):
    movie = Avmoo.objects(code=movie_code)
    return movie.__len__() > 0
