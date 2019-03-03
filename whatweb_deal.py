#coding=utf-8
f=open("temp.txt")
for i in f.readlines():
    i=i.rstrip("\n")
    #print(i)
    if "" not in i and "" not in i:
        print(i)
f.close()