#!/usr/bin/env python3

from flask import Flask, request
from flask_restful import Resource, Api
import json
app = Flask(__name__)
api = Api(app)

timeA = 0
prev_timeA = 0
used_timeA = 0
sttA = 0

timeB = 0
prev_timeB = 0
used_timeB = 0
sttB = 0 

timeC = 0
prev_timeC = 0
used_timeC = 0
sttC = 0

class ParkingServer(Resource):
    def handle(self, req):
        js = json.loads(req)['data']
        """ Global variable """
        global timeA, timeB, timeC, prev_timeA, prev_timeB, prev_timeC,used_timeA, used_timeB, used_timeC, sttA, sttB, sttC
        """ Parse data from request """
        timeA = int(js[0])
        timeB = int(js[1])
        timeC = int(js[2])
        print( timeA, '-', timeB, '-', timeC)
        """ Handling time value"""
        if timeA != 0:
            if prev_timeA != 0:
                used_timeA = timeA - prev_timeA
                prev_timeA = 0
                sttA = 0
            else:
                prev_timeA = timeA
                sttA = 1

        if timeB != 0:
            if prev_timeB != 0:
                used_timeB = timeB - prev_timeB
                prev_timeB = 0
                sttB = 0
            else:
                prev_timeB = timeB
                sttB = 1

        if timeC != 0:
            if prev_timeC != 0:
                used_timeC = timeC - prev_timeC
                prev_timeC = 0
                sttC = 0
            else:
                prev_timeC = timeC
                sttC = 1
    
    def post(self):
        req = request.data
        self.handle(req)
        return "Update success"

    def get(self):
        global sttA, sttB, sttC
        response = {"data": ["","",""]}
        response["data"][0] = sttA
        response["data"][1] = sttB
        response["data"][2] = sttC
        print(response)
        return response
    
api.add_resource(ParkingServer, '/')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 2685, debug = True)





