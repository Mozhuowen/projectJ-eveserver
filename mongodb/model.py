#!coding=utf-8
from mongoengine import *

print 'start to init mongodb...'
connect('stackoverflow', host='45.33.41.182', port=27017, username='avmoo', password='0603')
print 'finished init mongodb!'

class Movie(Document):
    semester = StringField()
    grades = ListField()

class Actress(Document):
    view_count = IntField()
    url_movies = StringField()
    image_cover_url = StringField()
    actressname = StringField()
    image_urls = ListField(StringField())
    actresscode = StringField()

class Avmoo(Document):
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

class Movies(Document):
    view_count = IntField()
    good_count = IntField()
    title = StringField()
    image_urls = ListField(StringField())
    url_detail = StringField()
    _etag = StringField()
    desc = StringField()
    _updated = DateTimeField()
    _deleted = BooleanField()
