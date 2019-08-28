"""
For writing logs into file specified by client

"""

import sys
from os.path import dirname as opd, realpath as opr
import os

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkgate.Config.Config import Config

class FileLogger:
	"""Class for writing logs into file"""

	@staticmethod
	def fileLogger(logger_object):
		"""
		Function tfor writing logs into file

		@return: True | False if file writing was successful or not
		"""
		with open(Config.getLogfile(), 'a+') as f:
			import json
			f.write("\n"+json.dumps(logger_object))
