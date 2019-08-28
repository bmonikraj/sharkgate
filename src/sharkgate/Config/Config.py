"""
config for the project
"""
import sys
from os.path import dirname as opd, realpath as opr
import os
import logging
logging.basicConfig(level=logging.INFO)

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

class Config:
	""" Config class for the whole project """

	HTTPLOG = True
	LOGGER = 'file'
	LOGFILE = '/sharkgate.log'
	DISCOVERY = 'static'
	SHARKRADARHOST = 'http://127.0.0.1:16461'
	POLICYDIR = '/'
	POLICIES = []
	MQHOST = 'localhost'
	MQPORT = 5672

	@staticmethod
	def getHTTPLog():
		return Config.HTTPLOG

	@staticmethod
	def setHTTPLog(httplog):
		logging.info("HTTPLog param set to '{0}'".format(httplog))
		if httplog=='y':
			Config.HTTPLOG = True
		else:
			Config.HTTPLOG = False

	@staticmethod
	def getLogger():
		return Config.LOGGER

	@staticmethod
	def setLogger(logger):
		logging.info("Logger param set to '{0}'".format(logger))
		Config.LOGGER = logger

	@staticmethod
	def getLogfile():
		return Config.LOGFILE

	@staticmethod
	def setLogfile(logfile):
		logging.info("Logfile set to '{0}'".format(logfile))
		Config.LOGFILE = logfile

	@staticmethod
	def getDiscovery():
		return Config.DISCOVERY

	@staticmethod
	def setDiscovery(discovery):
		logging.info("Discovery param set to '{0}'".format(discovery))
		Config.DISCOVERY = discovery

	@staticmethod
	def getSharkradarhost():
		return Config.SHARKRADARHOST

	@staticmethod
	def setSharkradarhost(sharkradarhost):
		logging.info("Sharkradarhost param set to '{0}'".format(sharkradarhost))
		Config.SHARKRADARHOST = sharkradarhost

	@staticmethod
	def getPolicydir():
		return Config.POLICYDIR

	@staticmethod
	def setPolicydir(policydir):
		logging.info("Policy dir param set to '{0}'".format(policydir))
		Config.POLICYDIR = policydir

	@staticmethod
	def getPolicies():
		return Config.POLICIES

	@staticmethod
	def setPolicies(policies):
		logging.info("Policies set from policies dir")
		Config.POLICIES = policies

	@staticmethod
	def getMQHost():
		return Config.MQHOST

	@staticmethod
	def setMQHost(mqhost):
		logging.info("Rabbit MQ host param set to '{0}'".format(mqhost))
		Config.MQHOST = mqhost

	@staticmethod
	def getMQPort():
		return Config.MQPORT

	@staticmethod
	def setMQPort(mqport):
		logging.info("Rabbit MQ port param set to '{0}'".format(mqport))
		Config.MQPORT = mqport