"""
For writing logs into file specified by client

"""

import sys
from os.path import dirname as opd, realpath as opr
import os

from sharkgate.Config.Config import Config



basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

class FileLogger:
	"""Class for writing logs into file"""

	@staticmethod
	def writeLogIntoFile(logger_object):
		"""
		Function tfor writing logs into file

		@return: True | False if file writing was successful or not
		"""
		pass




