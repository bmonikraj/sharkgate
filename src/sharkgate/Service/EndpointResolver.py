import sys
from os.path import dirname as opd, realpath as opr
import os
import requests
from flask import Response
import logging
logging.basicConfig(level=logging.INFO)

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkgate.Config.Config import Config

class EndpointResolver:
	"""
	"""
	def endpointResolver(src_path):
		return src_path