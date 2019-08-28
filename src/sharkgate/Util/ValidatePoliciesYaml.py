"""
Validate client input of address book elements for schema

"""

import sys
from os.path import dirname as opd, realpath as opr
import os
import logging
logging.basicConfig(level=logging.INFO)

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

class ValidatePoliciesYaml:
	"""Class to use discovery API of sharkradar"""

	@staticmethod
	def validatePoliciesYaml(ymlList):
		"""
		Function to fetch details of a micro-services from Service R/D, sharkradar

		@return: True | False if  publishing to MQ was successful or not
		"""
		status = True
		message = ""
		allowed_keys = ['name', 'source-url-pattern', 'target-host-address', 'target-sharkradar-name', 'target-sharkradar-protocol', 'authentication-enable', 'authentication-key']
		allowed_keys.sort()
		for obj in ymlList:
			present_keys = list(obj.keys())
			present_keys.sort()
			if present_keys != allowed_keys:
				status = False
				message = "Keys not as expected for policy object \n{0}".format(obj)
				return status, message
		return status, message