"""
Route request

"""

import sys
from os.path import dirname as opd, realpath as opr
import os

import requests
from sharkgate.Config.Config import Config


basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)


class RouteRequestProxy:
	"""Class for initiaitng request to api_endpoint and returning fetched response"""

	@staticmethod
	def routeRequest(api_endpoint, request_method, request_body, request_header):
	"""
		Function for initiaitng request to api_endpoint and returning fetched response
		@params: api_endpoint: api endpoint to which request will be routed
		@params: request_method: method of the request, e.g GET, POST etc
		@params: request_body : JOSN formatted request paramaters
		@params: request_type : Type of the request, e.g GET, POST etc


		@return: Response object fetched from api_endpoint
	"""

	#check in adddress book first
	address_book = Config.getAddressBook()
	r = {'status' : 'failure', 'res' : None}

	flag = 0

	for item in address_book:
		if item['virtual_endpoint'] == api_endpoint:
			endpoint_record = item
			flag = 1
			break

	if flag == 1:
		r['status'] = 'success'
	else:
		r['res'] = 'API endpoint not found in address_book'
		return r


	if Config.getEnableSRD():
		response_tuple = DiscoverSharkradar.discoverSharkradar(endpoint_record['actual_endpoint'])
		service_ip = response_tuple['ip']
		service_port = response_tuple['port']
		#initiate a request and send response

		host = 'http://' + ip + ':' + port
		URL = host + '/' + endpoint_record['actual_endpoint']

		if request_method == 'GET':
			#return request.get(url = host, params = request_body)
		elif request_method == 'POST':
			data = requests.post(url = host, data = request_body)
			r['res'] = data
			return r
	else:
		URL = endpoint_record['host'] + '/' + endpoint_record['actual_endpoint']
		if request_method == 'GET':
			#return request.get(url = host, params = request_body)
		elif request_method == 'POST':
			data = requests.post(url = host, data = request_body)
			r['res'] = data
			return r
