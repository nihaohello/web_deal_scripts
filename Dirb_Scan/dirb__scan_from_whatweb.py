#coding=utf-8
import re
import sys
import os
d=os.path.dirname(__file__)
base_file=os.path.dirname(d)
f=open(base_file+"/temp.txt",encoding="utf-8")
urls=[]
for i in f.readlines():
    i=i.rstrip("\n")
    i=i.split(" ")[0]
    i=str(re.findall("http.*cn",i))
    i=i.rstrip("']").lstrip("['")
    urls.append(str(i))
f.close()
print(len(urls))
with open("dirb_urls.txt","w") as f:
    for i in urls:
        f.write(i)
        f.write("\n")
f.close()