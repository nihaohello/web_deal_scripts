#coding=utf-8
import urllib.request
import re
f=open("login_admin_from_google.txt",encoding="utf-8")
sqlmap_urls=[]
m=f.read()
m=m.replace("\n","")
urls=re.findall(r'http.*?"',m)
compare=[]
for i in urls:
    i = urllib.request.unquote(i)
    i = i.replace('"', "").replace(";", "")
    if "login" in i or "admin" in "i" and "google" not in i and "gstatic" not in i:
        '''j=i.split('.')[0]
        if j not in compare:
            compare.append(j)
            #i=urllib.request.urlopen(i)
            '''
        sqlmap_urls.append(i)
        print(i.strip('"'))
f.close()
sql=list(set(sqlmap_urls))
login=[]
for i in sql:
    if "google" not in i:
        login.append(i)
with open("login_urls.txt","w+",encoding="utf-8") as f:
    for i in login:
        f.write(i)
        f.write("\n")
f.close()
