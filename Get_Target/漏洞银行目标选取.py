#coding=utf-8
import random
f=open("step1.txt")
urls=[]
for i in f.readlines():
    if "学" in i:
        urls.append(i.rstrip("\n"))
f.close()
m = random.randint(0, 100)
print(m)
print(urls[m])