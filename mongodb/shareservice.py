# -*- coding: utf-8 -*-

from datetime import datetime
from model import Share
import userservice
import movieservice


def create_share(userid='', content='', movie_code=''):
    if not userservice.check_user_exist(userid=userid):
        return {}, 0, 'user not exist!'

    if not movieservice.check_movie_exist(movie_code=movie_code):
         return {}, 0, 'movie not exist!'

    share = Share(userid=userid, content=content, movie_code=movie_code)
    share.save()
    return {
               'status': 1
           }, 1, ''
