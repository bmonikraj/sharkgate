"""
config for the project
"""
import sys
from os.path import dirname as opd, realpath as opr
import os

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)


from sharkgate.Util import ValidateAddressBook
class Config:
	""" Config class for the whole project """

	LOGGING_ENABLED = None #Bool for logging functionality
	SRD_ENABLED = None #Bool for Sercvice registry and discovery

	IP = "127.0.0.1" #Default IP on which sharkgate will be served
	PORT  =  9090 #Default PORT on which sharkgate will be served

	ADDRESS_BOOK = [] #To store api_endpoints from client

	@staticmethod
	def setIpAndPort(ip = Config.IP, port = Config.PORT):
	"""
		Setter for ip and port
	"""
		Config.IP = ip
		Config.PORT = port

	@staticmethod
	def setEnableLogging(enabled = True):
	"""
		Setter for Logging functonality. Default is true
	"""
		Config.LOGGING_ENABLED = enabled


	@staticmethod
	def getEnableLogging():
		"""
		Getter for logging enabling status
	"""
		if Config.LOGGING_ENABLED:
			return True
		return False

	@staticmethod
	def getEnableSRD():
		"""
		Getter for SRD enabling status
	"""
		if Config.SRD_ENABLED:
			return True
		return False


	@staticmethod
	def setEnableSRD(enabled= True):
	"""
		Setter for SRD method: Default is True
	"""
		Config.SRD_ENABLED = enabled


	@staticmethod
	def setHttpLogger(logger = "fileLogging", logger_file_url = ""):
	"""
		Setter for http logging method type
		===================================
		1. fileLogging : Logs in a local file specified by the client
		2. MqService : External messaging queue service
	"""
		if Config.LOGGING_ENABLED:
			Config.LOGGER = logger
			if logger == "fileLogging":
				Config.LOGGER_FILE_URL = logger_file_url
			return True
		else:
			return False

	@staticmethod
	def getHttpLogger():
	"""
		Getter for http logging method typr
	"""
	if Config.LOGGING_ENABLED:
		return Config.LOGGER
	else:
		return ""


	@staticmethod
	def getHttpLoggerFileUrl():
	"""
		Getter for http logger file url. (if Config.LOGGER is set to "fileLogging")
	"""
	if Config.LOGGING_ENABLED and Config.LOGGER == "fileLogging":
		return Config.LOGGER_FILE_URL
	else:
		return ""

	@staticmethod
	def setSrdIpAndPort(ip = "127.0.0.1", port = "16461"):
	"""
		Setter for sharkradar IP and PORT
	"""
		if Config.SRD_ENABLED:
			Config.SRD_IP = ip
			Config.SRD_PORT = port
			return True
		else:
			return False
	@staticmethod
	def getSrdIpAndPort():
	"""
		Getter for sharkradar IP and PORT
	"""
	if Config.SRD_ENABLED:
		ip = Config.SRD_IP
		port = Config.SRD_PORT
		return (ip, port)

	return ("", "")


	@staticmethod
	def setAddressBook(virtual_api_end_point, actual_api_end_point, host = ""):
	"""
		Insert data into address book
	"""
	address_book_element = {}
	address_book_element['virtual_endpoint'] = virtual_api_end_point
	address_book_element['actual_endpoint'] = actual_api_end_point

	if Config.SRD_ENABLED:
		address_book_element['host']  = ""
	else:
		address_book_element['host']  = host

	Config.ADDRESS_BOOK.append(address_book_element)

	@staticmethod
	def getElementFromAddressBookByVirtualEndpoint(virtual_api_end_point):
	"""
		Search for record in ADDRESS_BOOK with virtuak_api_end_point
	"""
		address_book = Config.ADDRESS_BOOK
		for item in address_book:
			if item['virtual_endpoint'] == virtual_api_end_point:
				return item['host']
		return ""

	@staticmethod
	def getAddressBook():
	"""
		Return ADDRESS_BOOK
	"""
	return Config.ADDRESS_BOOK
