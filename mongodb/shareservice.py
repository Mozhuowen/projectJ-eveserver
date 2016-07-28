# -*- coding: utf-8 -*-

from datetime import datetime
from model import Share, Simplemovie, Avmoo
import userservice
import movieservice


def create_share(userid='', content='', movie_code=''):
    if not userservice.check_user_exist(userid=userid):
        return {}, 0, 'user not exist!'

    if not movieservice.check_movie_exist(movie_code=movie_code):
         return {}, 0, 'movie not exist!'

    movie = Avmoo.objects(code=movie_code)[0]
    simple_movie = Simplemovie(movie_code=movie.code,
                               cover_image=movie.image_small_url,
                               actress=movie.actress[0]['name'])
    share = Share(userid=userid, content=content, movie=simple_movie)
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
    return shares.to_mongo(), 1, ''
