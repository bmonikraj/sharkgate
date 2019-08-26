"""
Validate client input of address book elements for schema

"""

import sys
from os.path import dirname as opd, realpath as opr
import os

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkgate.Config.Config import Config

file_list = os.listdir(basedir + '/dir/*.addressbook.yaml')

class ValidateAddressBook:
	"""Class to use discovery API of sharkradar"""

	@staticmethod
	def validateAddressBook():
		"""
		Function to fetch details of a micro-services from Service R/D, sharkradar

		@return: True | False if  publishing to MQ was successful or not
		"""
		#write code here
		pass






