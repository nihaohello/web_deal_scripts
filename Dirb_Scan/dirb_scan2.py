#coding=utf-8
#基于python多线程扫描
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from Dirb_Scan_Class import Dirb_Scan
base_path=os.path.dirname(os.path.abspath(__file__))
base_path=base_path+"/dirb_catlogs/"
if not os.path.exists(base_path):
    os.mkdir(base_path)
f=open("dirb_urls.txt")
urls=[]
wordlist="dirb_wordlist.txt"
if len(sys.argv) > 1:
    wordlist=sys.argv[2]
for i in f.readlines():
    if "http" in i:
        i=i.rstrip("\n")
        urls.append(i)
f.close()
urls=list(set(urls))
for url in urls:
    if (len(url.split("."))==4):
        url = url.split(".")[-4].lstrip("http://").lstrip("https://").rstrip("/")
        command="cat dirb_wordlist.txt >"+url+"_temp.txt"
        os.system(command)

for url in  urls:
    a=Dirb_Scan(url)
    a.run()
for url in urls:
    if (len(url.split("."))==4):
        url = url.split(".")[-4].lstrip("http://").lstrip("https://").rstrip("/")
        command="rm "+url+"_temp.txt"
        os.system(command)




