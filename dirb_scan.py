#coding=utf-8
import os
import sys
from concurrent.futures import ThreadPoolExecutor
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
        if  os.path.exists(url+"_temp.txt"):
            command="rm "+url+"_temp.txt"
            os.system(command)
#dirb
def Handler(urls):
    global command
    command=""
    for url in urls:
        dirb_temp = url.split(".")[-4].lstrip("http://").lstrip("https://").rstrip("/")
        command = command+" dirb " + url + " " + wordlist + " -z 50 -w -o " + dirb_temp + "_temp" + ".txt"
        command = command + " ;"
        command = command + " cat dirb_temp.txt >>  " + base_path  + dirb_temp + ".txt"
        command = command + " ;" + "rm dirb_temp.txt ;"
    command=command
    return command
dirb_command=Handler(urls)
print(dirb_command)
os.system(dirb_command)

#print(a)




