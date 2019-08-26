import sys
from os.path import dirname as opd, realpath as opr
import os
from flask import Flask, request

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkgate.Service.HttpLogger import HttpLogger
from sharkgate.Service.RouteRequestProxy import RouteRequestProxy

app = Flask(__name__)

@app.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
	HttpLogger.storeLogObject(request)
	response = RouteRequestProxy.RouteRequestProxy(request)
	HttpLogger.storeLogObject(response)
	return path

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)
