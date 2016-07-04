#!coding=utf-8

from mongoengine import *
import urllib2

# connect('stackoverflow', host='45.33.41.182', port=27017, username='avmoo', password='0603')

class Movie(Document):
    semester = StringField()
    grades = ListField()

def updatetitle(title):
    Movie(semester='test')

def test(request):
    print request.url
    print request.headers
    print request.args.get('test')
    data = Movie.objects(semester='test').update_one(push__grades=request.args.get('test'))
    print data,'test'
    return 'test'
    # print data.to_json()
    # return data.to_json()

def test2(doc):
    data = doc.objects(semester='test')
    return data.to_json()