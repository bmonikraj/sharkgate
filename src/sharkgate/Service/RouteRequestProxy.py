"""
Route request

"""

import sys
from os.path import dirname as opd, realpath as opr
import os
import requests

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkgate.Config.Config import Config

class RouteRequestProxy:
	"""Class for initiaitng request to api_endpoint and returning fetched response"""

	@staticmethod
	def RouteRequestProxy(flaskRequestObject):
		"""
			Function for initiaitng request to api_endpoint and returning fetched response
			@params: api_endpoint: api endpoint to which request will be routed
			@params: request_method: method of the request, e.g GET, POST etc
			@params: request_body : JOSN formatted request paramaters
			@params: request_type : Type of the request, e.g GET, POST etc


			@return: Response object fetched from api_endpoint
		"""
		"""
			POST, PUT, DELETE -> Complete URL can be remapped to new endpoint
			<src path> -> <new path> ===: (1)
			GET -> URL with query params or URL with path based params
			<src path?q1=x...> -> <new path> ===: (1)
			<src path/q1...> -> <new path/q1> ===: (2)
		"""
		print(flaskRequestObject.path) # src endpoint
		print(flaskRequestObject.args) # GET params
		print(flaskRequestObject.form) # POST, PUT, DELETE params
		print(flaskRequestObject.headers) # headers 
		print(flaskRequestObject.files) # file objects for POST, PUT

		# based on src endpoint - mapping (1) or (2) and get some target endpoint

		if flaskRequestObject.method == 'POST':
			pass
		if flaskRequestObject.method == 'PUT':
			pass
		if flaskRequestObject.method == 'DELETE':
			pass
		if flaskRequestObject.method == 'GET':
			pass


