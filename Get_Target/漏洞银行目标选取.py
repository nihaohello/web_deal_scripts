#coding=utf-8
import random
f=open("step1.txt",encoding="utf-8")
urls=[]
for i in f.readlines():
    if "网" in i:
        urls.append(i.rstrip("\n"))
f.close()
#print(len(urls))
m = random.randint(0,118)
print(m)
print(urls[m])

