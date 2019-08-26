"""
Validate client input of address book elements for schema

"""

import sys
from os.path import dirname as opd, realpath as opr
import os

from sharkgate.Config.Config import Config



basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

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
		for file in file_list:
			with open(file, 'r') as f:
				
				
			f.close()

		# Read files from dir one by one. Check for files with .addressBook.yaml extension
		# Append the result and and insert into ADDRESS_BOOK






