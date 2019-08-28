"""
For writing logs into MQ specified by client

"""

import sys
from os.path import dirname as opd, realpath as opr
import os
import pika
import json

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkgate.Config.Config import Config

class MQLogger:
	"""Class for writing logs into MQ"""

	@staticmethod
	def mqLogger(logger_object):
		"""
		Function or writing logs into MQ

		@return: True | False if  publishing to MQ was successful or not
		"""
		#write code here
		connection = pika.BlockingConnection(pika.ConnectionParameters(Config.getMQHost(), Config.getMQPort()))
		channel = connection.channel()
		channel.exchange_declare(exchange='sharkgate',
                         exchange_type='topic')
		channel.basic_publish(exchange='sharkgate',
                      routing_key='httplogs',
                      body=json.dumps(logger_object),
                      properties=pika.BasicProperties(
                         delivery_mode = 2,
                      ))
		connection.close()
