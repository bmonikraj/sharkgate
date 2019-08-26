"""
For interacting with sharkradar using discovery API of sharkradar

"""

import sys
from os.path import dirname as opd, realpath as opr
import os

from sharkgate.Config.Config import Config
import requests

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

class DiscoverSharkradar:
	"""Class to use discovery API of sharkradar"""

	@staticmethod
	def discoverSharkradar(service_name):
		"""
		Function to fetch details of a micro-services from Service R/D, sharkradar

		@params: service_name: Unique service name of the micro-service
		@return: A tuple containing ip and port of the active micro-service instance
		"""
		pass


