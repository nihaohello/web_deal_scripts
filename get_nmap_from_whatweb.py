#coding=utf-8
import re
f=open("temp.txt",encoding="utf-8")
urls=[]
for i in f.readlines():
    i=i.rstrip("\n")
    #print(i)
    urls.append(i)
f.close()
urls1=[]
for i in urls:
    if "IP" in i:
        if len(re.findall("IP.*?,", i)) !=0:
            a=re.findall("IP.*?,",i)[0].lstrip("IP[").rstrip("],")
            urls1.append(a)
    #if "200" in i:
        #print i
urls2=set(urls1)
with open("nmap_ips.txt","w") as f:
    for i in urls2:
        print(i)
        f.write(i)
        f.write("\n")
f.close()