#! /usr/bin/python
# -*- encoding: utf-8 -*-
# @Author: DZF

import BaseService
import requests
import logging

class BalanceService(BaseService.BaseService):
	POST_BALANCE = 'balance'

	def __init__(self):
		super(BalanceService, self).__init__('Balance')