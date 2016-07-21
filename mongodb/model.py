#!coding=utf-8
from mongoengine import *
from util.JJQuerySet import *
from util.JJDocument import *

print 'start to init mongodb...'
connect('stackoverflow', host='45.33.41.182', port=27017, username='avmoo', password='0603')
print 'finished init mongodb!'


class Movie(Document):
    meta = {'queryset_class': JJQuerySet}
    semester = StringField()
    grades = ListField()


class Actress(Document):
    meta = {'queryset_class': JJQuerySet}
    view_count = IntField()
    url_movies = StringField()
    image_cover_url = StringField()
    actressname = StringField()
    image_urls = ListField(StringField())
    actresscode = StringField()


class Avmoo(Document):
    meta = {'queryset_class': JJQuerySet}
    publisher = DictField()
    code = StringField()
    title = StringField()
    series = DictField()
    publishtime = StringField()
    image_urls = ListField(StringField())
    director = DictField()
    length = StringField()
    url_detail = StringField()
    actress = ListField(DictField())
    genre = ListField(DictField())
    image_small_url = StringField()
    maker = DictField()
    image_large_url = StringField()
    like_count = IntField()
    sample_images = ListField(StringField())


class Movies(Document):
    meta = {'queryset_class': JJQuerySet}
    view_count = IntField()
    good_count = IntField()
    title = StringField()
    image_urls = ListField(StringField())
    url_detail = StringField()
    _etag = StringField()
    desc = StringField()
    _updated = DateTimeField()
    _deleted = BooleanField()
    test_data = DateTimeField()
    semester = StringField()
    grades = ListField()


class User(Document):
    meta = {'queryset_class': JJQuerySet}
    email = StringField()
    passwd = StringField()
    userid = StringField()
    deviceid = StringField()
    device_ids = ListField()
    avater = StringField()
    nick_name = StringField()
    signature = StringField()
    location = StringField()
    location_geo = GeoPointField()
    likemovie = ListField()
    likeactress = ListField()
    viewmoviehis = ListField()
    viewactresshis = ListField()
    createdate = DateTimeField()
    logindate = DateTimeField()
    haslogin = IntField()
    sex = IntField()
    follow_count = IntField()
    fans_count = IntField()
    share_count = IntField()


class Like(Document):
    meta = {'queryset_class': JJQuerySet}
    userid = StringField()
    movie_code = StringField()
    movieid = StringField()
    update_time = DateTimeField()
    valid = IntField()
