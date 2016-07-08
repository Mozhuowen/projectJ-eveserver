#!coding=utf-8

from mongoengine import Document
import helper


class JJDocument(Document):

    def to_dict(self):
        return helper.mongo_to_dict(self, [])
