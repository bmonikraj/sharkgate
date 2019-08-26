"""
config for the project
"""
import sys
from os.path import dirname as opd, realpath as opr
import os

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

class Config:
	""" Config class for the whole project """

	LOGGING = 'y'
	LOGGER = 'file'
	LOGFILE = '/'
	DISCOVERY = 'static'
	SHARKRADARHOST = 'http://127.0.0.1:16461'
	CONFIGDIR = '/'

	@staticmethod
	def getLogging():
		return Config.LOGGING

	@staticmethod
	def setLogging(logging):
		if logging=='y':
			Config.LOGGING = True
		else:
			Config.LOGGING = False

	@staticmethod
	def getLogger():
		return Config.LOGGER

	@staticmethod
	def setLogger(logger):
		Config.LOGGER = logger

	@staticmethod
	def getLogfile():
		return Config.LOGFILE

	@staticmethod
	def setLogfile(logfile):
		Config.LOGFILE = logfile

	@staticmethod
	def getDiscovery():
		return Config.DISCOVERY

	@staticmethod
	def setDiscovery(disovery):
		Config.DISCOVERY = disovery

	@staticmethod
	def getSharkradarhost():
		return Config.SHARKRADARHOST

	@staticmethod
	def setSharkradarhost(sharkradarhost):
		Config.SHARKRADARHOST = sharkradarhost

	@staticmethod
	def getConfigdir():
		return Config.CONFIGDIR

	@staticmethod
	def setConfigdir(configdir):
		Config.CONFIGDIR = configdir