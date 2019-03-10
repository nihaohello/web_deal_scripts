#coding=utf-8
f=open("test.txt")
urls=[]
for i in f.readlines():
    urls.append(i.rstrip("\n"))
f.close()

urls1=[]
for i in urls:
    if i not in urls1:
        urls1.append(i)
        print(i)
