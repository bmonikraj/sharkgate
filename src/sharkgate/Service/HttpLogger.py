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
	def storeLogObject(flaskHTTPObject):
		"""
		Function to store log objects in user defined logger

		@params: log_object: Log object which will be stored in logger
		@return: True | False depiciting if storing the log was successful or not
		"""
		pass
