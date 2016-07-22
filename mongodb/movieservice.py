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

    like = Like.objects(userid=userid, movie_code=movie_code)
    if like.__len__() > 0:
        like = like[0]
        like.valid = 1
        like.update_time = datetime.now()
    else:
        like = Like(userid=userid, movie_code=movie.code, movieid=str(movie.id), valid=1, update_time=datetime.now())
    like.save()

    if movie.like_count is None:
        movie.like_count = 1
    else:
        movie.like_count += 1
    movie.save()
    return {}, 1, ''


def dislike_movie(userid='', movie_code=''):
    if not userservice.check_user_exist(userid=userid):
        return {}, 0, '用户不存在'

    if not check_movie_exist(movie_code=movie_code):
        return {}, 0, '影片不存在'

    like = Like.objects(userid=userid, movie_code=movie_code)
    if like.__len__() == 0:
        return {}, 0, '未收藏该影片'

    movie = Avmoo.objects(code=movie_code)[0]
    movie.like_count -= 1
    movie.save()

    like = like[0]
    like.valid = 0
    like.save()
    return {}, 1, ''


def get_like_status(userid='', movie_code=''):
    like = Like.objects(userid=userid, movie_code=movie_code, valid=1)
    if like.__len__() > 0:
        return {
            'status': 1
        }, 1, ''
    else:
        return {
            'status': 0
        }, 1, ''


def get_user_like(userid='', page=1):
    likes = Like.objects(userid=userid, valid=1)
    if likes.__len__() == 0:
        return {}, 1, ''

    perPage = 26
    like_codes = [i['movie_code'] for i in likes]
    movies = Avmoo.objects(code__in=like_codes)[(page-1) * perPage:(page * perPage)-1]
    return movies.to_mongo(), 1, ''


def check_movie_exist(movie_code=''):
    movie = Avmoo.objects(code=movie_code)
    return movie.__len__() > 0
