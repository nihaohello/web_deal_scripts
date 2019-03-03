#coding=utf-8
f=open("temp.txt")
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
with open("IIS_AND_Nginx_urls.txt","w") as f:
    for i in urls2:
        f.write(i)
        f.write("\n")
f.close()


