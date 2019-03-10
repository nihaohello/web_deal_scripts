#coding=utf-8
f=open("temp.txt",encoding="utf-8")
urls=[]
for i in f.readlines():
    i=i.rstrip("\n")
    #print(i)
    #if "Unassigned" not in i and "500" not in i:
    if "Unassigned" not in i  and "Not Found" not in i and "ERROR" not in i:
        urls.append(i)
        print(i)
f.close()
with open("whatweb_result.txt","w+",encoding="utf-8") as f:
    for i in urls:
        f.write(i)
        f.write("\n")
f.close()

