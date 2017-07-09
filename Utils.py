#! /usr/bin/python
# -*- encoding: utf-8 -*-
# @Author: DZF
import hashlib
import hmac
import time

#Nonce Length
JUBI_NONCE_LENGHT = 12
JUBI_PARAMETER_ORDER = ['nonce', 'since', 'key', 'coin', 'type']

def getMd5Hash(s):
	m = hashlib.md5()
	m.update(s)
	return m.hexdigest()

def generate_nonce_from_timestamp():
	current_timestamp = time.time() * 100
	return str(long(current_timestamp))

generate_nonce = generate_nonce_from_timestamp

def generate_signature(msg, private_key):
	msg = bytes(msg).encode('utf-8')
	k = bytes(getMd5Hash(private_key)).encode('utf-8')
	signature = hmac.new(k, msg, digestmod = hashlib.sha256).hexdigest()
	return signature

def reformat_params(params, private_key, specific_setting_order = None):
	order = specific_setting_order if specific_setting_order else JUBI_PARAMETER_ORDER
	param_str = '&'.join(['%s=%s' % (name, params[name]) for name in order if params.has_key(name)])
	signature = generate_signature(param_str, private_key)
	params['signature'] = signature
	return params

if __name__ == '__main__':
	pass


