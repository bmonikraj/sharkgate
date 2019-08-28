import sys
from os.path import dirname as opd, realpath as opr
import os
import requests
from flask import Response
import re
import logging
logging.basicConfig(level=logging.INFO)

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkgate.Config.Config import Config

class EndpointResolver:
	"""
	"""
	def endpointResolver(src_path):
		policies = Config.getPolicies()
		for policy in policies:
			print(policy['source-url-pattern'], src_path)
			if re.search(policy['source-url-pattern'], src_path):
				if Config.getDiscovery() == 'static':
					logging.info("Static Endpoint fetched for {0}".format(src_path))
					return policy['target-host-address']+src_path
				else:
					srd_result = requests.get(url = Config.getSharkradarhost()+"/discovery/start/"+policy['target-sharkradar-name'])
					logging.info("Dynamic Endpoint fetched for {0}".format(src_path))
					return policy['target-sharkradar-protocol']+"://"+srd_result.json()['ip']+":"+srd_result.json()['port']+src_path
		logging.error("Source endpoint pattern not found for {0}".format(src_path))
		logging.warning("Endpoint address set <NOT_FOUND> for {0}".format(src_path))
		return '<NOT_FOUND>'