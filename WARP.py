#MODULES
import argparse
import requests
import httplib2
import sys
import itertools
import time
import threading
import icmplib
from icmplib import ping, multiping, traceroute, resolve
from html.parser import HTMLParser

start = input("1)PING IP\n 2)IP RANGE SCANNING\n")


#PING SCRIPT
if start == "1"  :
    addr = input("ADDR : ")
    valueConnect = ping(addr, count=4, interval=1, timeout=2, id=None, source=None, family=None, privileged=True)   
    if valueConnect.packets_received > 0 :           
        print(valueConnect)
    if valueConnect.packets_received == 0 :
        print("HOST SEEMS DOWN\n")

#IP RANGE SCANNING SCRIPT
if start == "2":
    print("this functionality is coming soon")

if start == "3" :
        url = input("URL: ") #user gets the url from here and stock it inside the url variable
        x = requests.get(url) #requests module import the html codde
        print(x.text) #print x  

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data) 

if start == "4" : #script to analyze a raw and unstructured data
    f = open("output.txt","r")  #the user open a file
    htmlInput = f  #test with a file
    parser = MyHTMLParser()
    #parser.feed()
    #test
    with open('output.txt' , "r") as b:
        with print(f.read()) as f :
            parser.feed(b) #test