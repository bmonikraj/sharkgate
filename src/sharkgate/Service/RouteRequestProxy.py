"""
Route request

"""

import sys
from os.path import dirname as opd, realpath as opr
import os
import requests
from flask import Response
import logging
logging.basicConfig(level=logging.INFO)

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkgate.Config.Config import Config
from sharkgate.Service.EndpointResolver import EndpointResolver

class RouteRequestProxy:
	"""Class for initiaitng request to api_endpoint and returning fetched response"""

	@staticmethod
	def RouteRequestProxy(flaskRequestObject):
		"""
			Notes on Basic HTTP Rules: 
			Supported Auth -> Custom with headers (Not HTTP based Auth) 
			Supported Methods -> GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH
			Timeout -> Disabled
			Redirection -> False
			Proxy -> Disabled
			TLS Verify -> Disabled
			Stream -> Disabled
			Cert -> Disabled
			Files -> (name, (filename, fileobj, content_type))
		"""
		"""
			POST, PUT, DELETE -> Complete URL can be remapped to new endpoint
			<src path> -> <new path> ===: (1)
			GET -> URL with query params or URL with path based params
			<src path?q1=x...> -> <new path> ===: (1)
			<src path/q1...> -> <new path/q1> ===: (2)
		"""
		# print(flaskRequestObject.path) # src endpoint
		# print(flaskRequestObject.args) # GET params
		# print(flaskRequestObject.form) # POST, PUT, DELETE params
		# print(flaskRequestObject.headers) # headers 
		# print(flaskRequestObject.files) # file objects for POST, PUT

		# based on src endpoint - mapping (1) or (2) and get some target endpoint
		files = {}
		for f in flaskRequestObject.files:
			files[f] = (flaskRequestObject.files[f].filename, flaskRequestObject.files[f].read(), flaskRequestObject.files[f].content_type)
		logging.info("Setting Request Object")
		targetURL = EndpointResolver.endpointResolver(flaskRequestObject.path)
		response = requests.request(
		 	method = flaskRequestObject.method,
		 	url = targetURL,
		 	params = flaskRequestObject.args.to_dict(),
		 	data = flaskRequestObject.form.to_dict(),
		 	headers = dict(flaskRequestObject.headers),
		 	cookies = dict(flaskRequestObject.cookies),
		 	files = files,
		 	allow_redirects = False)
		logging.info("Setting Response Object")
		responseHeaders = dict(response.headers)
		if 'Connection' in responseHeaders:
			responseHeaders.pop('Connection')
		if 'Keep-Alive' in responseHeaders:
			responseHeaders.pop('Keep-Alive')
		if 'Proxy-Authenticate' in responseHeaders:
			responseHeaders.pop('Proxy-Authenticate')
		if 'Proxy-Authorization' in responseHeaders:
			responseHeaders.pop('Proxy-Authorization')
		if 'TE' in responseHeaders:
			responseHeaders.pop('TE')
		if 'Trailers' in responseHeaders:
			responseHeaders.pop('Trailers')
		if 'Transfer-Encoding' in responseHeaders:
			responseHeaders.pop('Transfer-Encoding')
		if 'Upgrade' in responseHeaders:
			responseHeaders.pop('Upgrade')
		flaskResponseObject = Response(
								response = response.content,
								headers = responseHeaders,
								)
		flaskResponseObject.status_code = response.status_code
		for cookie in response.cookies:
			flaskResponseObject.set_cookie(cookie.name, cookie.value)
		return flaskResponseObject