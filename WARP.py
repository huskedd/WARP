import argparse
import requests
import httplib2
import sys
import itertools
import time
import threading
import icmplib
from icmplib import ping, multiping, traceroute, resolve
f = open("output.txt", "a")

start = input("1)SERVICE ENUMERATION\n 2)IP RANGE SCANNING\n")
#loading function


if start == "1"  :
    addr = input("ADDR : ")
    valueConnect = ping(addr, count=4, interval=1, timeout=2, id=None, source=None, family=None, privileged=True)   
    if valueConnect.packets_received > 0 :           
        print(valueConnect)
       
if start == "2":
    #code

    
    f.write(str(valueConnect))
    
if valueConnect.packets_received == 0:
                print("PING ERROR COULDN'T RESOLVE HOSTNAME")
                f.write(str(valueConnect))

f.close()   
