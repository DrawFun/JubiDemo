#! /usr/bin/python
# -*- encoding: utf-8 -*-
# @Author: DZF
import hashlib
import hmac
import time

#Nonce Length
JUBI_NONCE_LENGHT = 12
JUBI_PARAMETER_ORDER = ['nonce', 'key']

def getMd5Hash(s):
	m = hashlib.md5()
	m.update(s)
	return m.hexdigest()

def getHex(s):
	def _translate(ch):
		hv = hex(ord(ch)).replace('0x', '')
		if len(hv) == 1: hv = '0' + hv
		return hv
	return ''.join([_translate(x) for x in s])

def generate_nonce_from_timestamp():
	current_timestamp = time.time() * 100
	return str(long(current_timestamp))

generate_nonce = generate_nonce_from_timestamp

def generate_signature(msg, private_key):
	msg = bytes(msg).encode('utf-8')
	k = bytes(getMd5Hash(private_key)).encode('utf-8')
	signature = hmac.new(k, msg, digestmod = hashlib.sha256).digest()
	hex_signature = getHex(signature)
	return hex_signature

def reformat_params(params, private_key):
	param_str = '&'.join(['%s=%s' % (name, params[name]) for name in JUBI_PARAMETER_ORDER if params.has_key(name)])
	signature = generate_signature(param_str, private_key)
	params['signature'] = signature
	return params

if __name__ == '__main__':
	pass


