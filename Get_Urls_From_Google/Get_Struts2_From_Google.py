#coding=utf-8
import urllib.request
import re
f=open("struts2_result_from_google.txt",encoding="utf-8")
sqlmap_urls=[]
m=f.read()
m=m.replace("\n","")
urls=re.findall(r'http.*?"',m)
compare=[]
for i in urls:
    if "google" not in i and "gstatic" not in i :
        i=urllib.request.unquote(i)
        i=i.replace('"',"").replace(";","")
        j=i.split()
        if j not in compare:
            compare.append(j)
            #i=urllib.request.urlopen(i)
            sqlmap_urls.append(i)
            print(i.strip('"'))
f.close()
sql=list(set(sqlmap_urls))
with open("struts2_urls","w+",encoding="utf-8") as f:
    for i in sql:
        f.write(i)
        f.write("\n")
f.close()
