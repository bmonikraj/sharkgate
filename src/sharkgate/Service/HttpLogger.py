"""
Logging http request/response logs object

"""

import sys
from os.path import dirname as opd, realpath as opr
import os

from sharkgate.Config.Config import Config
from sharkgate.Util import FileLogger
from sharkgate.Util import MQLogger

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)


class HttpLogger:
	"""Class for storing logs object"""

	@staticmethod
	def storeLogObject(api_endpoint, request_method, log_object_type):
		"""
		Function to store log objects in user defined logger

		@params: log_object: Log object which will be stored in logger
		@return: True | False depiciting if storing the log was successful or not
		"""
		if Config.getEnableLogging():
			logging_object = {"request_method": request_method, "api_endpoint" : api_endpoint, "action_type" : log_object_type}

			logger = Config.getHttpLogger()
			if logger == "fileLogging":
				FileLogger.writeLogIntoFile(logging_object)
				#open file and store the log
			elif logger == "MqService":
				#use external messaging queue application. e.g rabbitMQ
				MQLogger.publishLogIntoMQ(logging_object)
			return True
		else:
			return False
