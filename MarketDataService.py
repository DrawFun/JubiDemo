#! /usr/bin/python
# -*- encoding: utf-8 -*-
# @Author: DZF

import BaseService
import requests
import logging

class MarketDataService(BaseService.BaseService):
	PATH_GET_TICKER = 'ticker'

	def __init__(self):
		super(MarketDataService, self).__init__('MarketData')

	def get_ticker(self, coin):
		param = {'coin' : coin}
		url = self.restful_url + MarketDataService.PATH_GET_TICKER
		self.logger.info('get_ticker: %s' % url)
		response = requests.get(url, params = param)
		return response.content if response else ''

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	marketDataService = MarketDataService()
	ticker = marketDataService.get_ticker('btc')
	print ticker
	assert(len(ticker))