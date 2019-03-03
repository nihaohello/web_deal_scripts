#coding=utf-8
import os
import sys
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
    i=i.rstrip("\n")
    urls.append(i)
f.close()
command2 = "rm dirb_temp.txt"
os.system(command2)
#dirb
a=1000
for url in urls:
    command="dirb "+url+" "+wordlist+" -z 50 -w -o dirb_temp.txt"
    os.system(command)
    url = url.split(".")[-1]
    if os.path.exists(base_path+"/"+url+".txt"):
        url=str(a)
        a=int(a)+1
    command1="cat dirb_temp.txt >>  "+base_path+"/"+url+".txt"
    os.system(command1)

