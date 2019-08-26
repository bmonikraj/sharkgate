"""
For writing logs into MQ specified by client

"""

import sys
from os.path import dirname as opd, realpath as opr
import os

from sharkgate.Config.Config import Config



basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

class MQLogger:
	"""Class for writing logs into MQ"""

	@staticmethod
	def publishLogIntoMQ(logger_object):
		"""
		Function or writing logs into MQ

		@return: True | False if  publishing to MQ was successful or not
		"""
		#write code here
		




