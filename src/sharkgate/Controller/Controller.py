from flask import Flask, request

from sharkgate.Service.HttpLogger import HttpLogger
from sharkgate.Service.RouteRequestProxy import RouteRequestProxy
from sharkgate.Util import DiscoverSharkradar
from sharkgate.Config.Config import Config

app = Flask(__name__)

@app.route('/proxy', methods = ['POST'])
def proxy():

	api_endpoint = request.path #http://vidur.com/entitlement-micro-service
	request_method = request.method
	request_header = request.headers
	request_body = request.form['request_body'] #JSON object containing request parameters as keys and their values

	
	HttpLogger.storeLogObject(api_endpoint, request_method, log_object_type = 'request_log')

	res = RouteRequestProxy.routeRequest(api_endpoint, request_method, request_header, request_body)

	HttpLogger.storeLogObject(api_endpoint, request_method, log_object_type = 'response_log')

	return res




if __name__ == '__main__':
   app.run()