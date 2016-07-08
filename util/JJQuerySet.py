#!coding=utf-8
from mongoengine.queryset import QuerySet


class JJQuerySet(QuerySet):

    def to_mongo(self):
        return self.as_pymongo()
