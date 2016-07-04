#!coding=utf-8

import mongoutil2
import model
import service

if __name__ == '__main__':

    data = service.findAllObjects(model.Movie)
    print data.to_json()

    data = service.findObjectById(model.Movie, '576f9c84cf00ee1cbea3a660')
    print data.to_json()