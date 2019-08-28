"""
Logging http request/response logs object

"""
import sys
from os.path import dirname as opd, realpath as opr
import os
import time
import logging
logging.basicConfig(level=logging.INFO)

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkgate.Config.Config import Config
from sharkgate.Util.FileLogger import FileLogger
from sharkgate.Util.MQLogger import MQLogger

class HttpLogger:
	"""Class for storing logs object"""

	@staticmethod
	def logger(flaskHTTPRequest, flaskHTTPResponse):
		"""
		Function to store log objects in user defined logger

		@params: log_object: Log object which will be stored in logger
		@return: True | False depiciting if storing the log was successful or not
		"""
		if Config.getHTTPLog():
			logObject = {}
			logObject['timestamp'] = str(time.ctime(time.time()))
			logObject['host'] = flaskHTTPRequest.host
			logObject['method'] = flaskHTTPRequest.method
			logObject['fullpath'] = flaskHTTPRequest.full_path
			logObject['status'] = flaskHTTPResponse.status_code
			logObject['size'] = flaskHTTPResponse.content_length
			logObject['request-headers'] = dict(flaskHTTPRequest.headers)
			logObject['response-headers'] = dict(flaskHTTPResponse.headers)
			logging.info("HTTP Logging ...")
			if Config.getLogger() == 'file':
				FileLogger.fileLogger(logObject)
			if Config.getLogger() == 'MQ':
				MQLogger.mqLogger(logObject)
