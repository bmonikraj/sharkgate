import sys
from os.path import dirname as opd, realpath as opr
import os
import yaml
import logging
logging.basicConfig(level=logging.INFO)

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkgate.Config.Config import Config
from sharkgate.Util.ValidatePoliciesYaml import ValidatePoliciesYaml

class PolicySetter:
	"""
	"""
	@staticmethod
	def policySetter():
		list_of_yml_doc = []
		for subdir, dirs, files in os.walk(Config.getPolicydir()):
		    for file in files:
		        filepath = subdir + os.sep + file
		        if filepath.endswith(".policy.yml"):
		            yml_docs = yaml.load_all(open(filepath, 'r'), Loader=yaml.Loader)
		            for ydocs in yml_docs:
		            	list_of_yml_doc.append(ydocs)
		status, message = ValidatePoliciesYaml.validatePoliciesYaml(list_of_yml_doc)
		if status:
			logging.info("{0} Policies set successfully".format(len(list_of_yml_doc)))
			Config.setPolicies(list_of_yml_doc)
		else:
			logging.error(message)
			logging.warning("sharkgate shutting down ...")
			sys.exit(101)