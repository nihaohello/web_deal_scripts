#coding=utf-8
import os
d=os.path.dirname(__file__)
base_file=os.path.dirname(d)
f=open(base_file+"/temp.txt",encoding="utf-8")
print(f)
urls=[]
urls1=[]
urls2=[]
for i in f.readlines():
    i=i.rstrip("\n")
    #print(i)
    urls.append(i)
f.close()
print("Apache:")
for i in urls:
    if "Apache" in i:
        urls1.append(i)
        print(i)
print("IIS_Nginx:")
for i in urls:
    if "Apache" not in i:
        urls2.append(i)
        print(i)
with open("Apache_urls.txt","w") as f:
    for i in urls1:
        f.write(i)
        f.write("\n")
f.close()
with open("IIS_AND_Nginx_urls.txt","w",encoding="utf-8") as f:
    for i in urls2:
        f.write(i)
        f.write("\n")
f.close()

