#! /usr/bin/python
# -*- encoding: utf-8 -*-
# @Author: DZF

import json

class BaseService(object):
	def __init__(self):
		try:
			f = open('conf.json', 'r')
			conf = json.load(f)
			self.base_url = conf['base_url'] 
			self.api_url = conf['api_url']
			self.restful_url = self.base_url + self.api_url + '%s'
		except Exception as e:
			raise