#coding=utf-8
import re
import sys
f=open("temp.txt")
urls=[]
wordlist="/root/dict/web/wordlist1.txt"
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