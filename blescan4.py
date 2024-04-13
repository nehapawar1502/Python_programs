# test BLE Scanning software
# jcs 6/8/2014
import json
import blescan
import sys
import requests
import time
from datetime import datetime as dt
listuuid =[]
DEBUG=1
import bluetooth._bluetooth as bluez
dev_id = 0
try:
        sock = bluez.hci_open_dev(dev_id)
        print ("ble thread started")

except:
        print ("error accessing bluetooth device...")
        sys.exit(1)
try:
        blescan.hci_le_set_scan_parameters(sock)
        blescan.hci_enable_le_scan(sock)
        flag=1
        lst = []
        while True:
                try:
                        dt.now()
                        min=dt.now().minute
                        sec=dt.now().second
                        returnedList = blescan.parse_events(sock, 10)
                        #lst= [returnedList]
                        #emp_json =json.dumps(lst)
                        #payload = {'json_payload': emp_json}
                        #r = requests.post('http://nakshatratechnology.org/attendance.php',payload)
                        #print r.status_code
                        #print r.text[:300]

                        #print "----------"
                        #lst = []
                        for beacon in returnedList:
                                emp  = beacon[0:3]
                                uuid = beacon[0:32]
                                power= beacon[32:35]
                                if uuid not in listuuid:
                                        if "E1D492F7DA4451B485" in uuid or "e1d492f7da4451b485" in uuid :
                                                print(uuid)
                                                listuuid.append(uuid)
                                                lst=set(listuuid)
                                                lst = list(lst)
                        if min%5==0 and len(lst)>0 and flag==1:
                                print (list)
                                emp_json =json.dumps(lst)
                                payload = {'InputJson': emp_json}
                                # r = requests.post('https://wsg.writercorporation.com/OPUS/api/Login/markAttendance?InputJson='+emp_json)
                                flag =0

                                # print( r.status_code)
                                # print r.text[:300]
                                # if r.status_code == 200:
                                #         listuuid=[]
                                #         lst=[]
                                        #time.sleep(60)
                                        #print beacon
                        elif min%5!=0 and flag==0:
                                flag=1
                except Exception as e: print(e)
except:
        print ("Exception")

