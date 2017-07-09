#! /usr/bin/python
# -*- encoding: utf-8 -*-
# @Author: DZF

import requests
import logging
import json
import BaseService
import Utils

class BalanceService(BaseService.BaseService):
	POST_BALANCE = 'balance'

	def __init__(self):
		super(BalanceService, self).__init__('Balance')
		try:
			f = open('keys.json', 'r')
			conf = json.load(f)
			self.public_key = conf['query']['public_key'] 
			self.private_key = conf['query']['private_key']
		except Exception as e:
			raise

	def post_balance(self):
		nonce = Utils.generate_nonce()
		original_params = {'nonce' : nonce, 'key' : self.public_key}
		params = Utils.reformat_params(original_params, self.private_key)
		print params
		url = self.restful_url + BalanceService.POST_BALANCE
		self.logger.info('post_balance: %s' % url)
		response = requests.post(url, data = params)
		return response.content if response else ''			

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	balanceService = BalanceService()
	balance = balanceService.post_balance()
	print balance