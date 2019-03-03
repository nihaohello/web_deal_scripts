#coding=utf-8
import random
f=open("temp.txt")
urls=[]
for i in f.readlines():
    urls.append(i.rstrip("\n"))
f.close()
m = random.randint(0,10)
print(m)
temp=urls[m]
print(temp)
urls.remove(temp)
with open("temp1.txt","a+") as f2:
    f2.write(temp)
    f2.write("\n")
f2.close()

with open("temp.txt","w") as f1:
    for i in urls:
        f1.write(i)
        f1.write("\n")
f1.close()