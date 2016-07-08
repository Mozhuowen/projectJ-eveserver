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

    # def to_json(self):
    #     return {
    #         'semester': self.semester,
    #         'grades': self.grades
    #     }


class Actress(Document):
    meta = {'queryset_class': JJQuerySet}
    view_count = IntField()
    url_movies = StringField()
    image_cover_url = StringField()
    actressname = StringField()
    image_urls = ListField(StringField())
    actresscode = StringField()

    # def to_json(self):
    #     return {
    #         'view_count': self.view_count,
    #         'url_movies': self.url_movies,
    #         'image_cover_url': self.image_cover_url,
    #         'actressname': self.actressname,
    #         'image_urls': self.image_urls,
    #         'actresscode': self.actresscode
    #     }


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

    # def to_json(self):
    #     return {
    #         'publisher': self.publisher,
    #         'code': self.code,
    #         'title': self.title,
    #         'series': self.series,
    #         'publishtime': self.publishtime,
    #         'image_urls': self.image_urls,
    #         'director': self.director,
    #         'length': self.length,
    #         'url_detail': self.url_detail,
    #         'actress': self.actress,
    #         'genre': self.genre,
    #         'image_small_url': self.image_small_url,
    #         'maker': self.maker,
    #         'image_large_url': self.image_large_url
    #     }


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

    # def to_json(self):
    #     return {
    #         'view_count': self.view_count,
    #         'good_count': self.good_count,
    #         'title': self.title,
    #         'image_urls': self.image_urls,
    #         'url_detail': self.url_detail,
    #         '_etag': self._etag,
    #         'desc': self.desc,
    #         '_updated': self._updated,
    #         '_deleted': self._deleted,
    #         # 'test_data': self.test_data.time()
    #     }


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
