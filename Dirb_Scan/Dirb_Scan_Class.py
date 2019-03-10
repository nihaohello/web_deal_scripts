#coding=utf-8
import requests
import os
from concurrent.futures import ThreadPoolExecutor
base_path=os.path.dirname(os.path.abspath(__file__))
base_path=base_path+"/dirb_catlogs/"
class Dirb_Scan(object):
    def __init__(self,url):
        self.url=url
        self.dirb_temp = url.split(".")[-4].lstrip("http://").lstrip("https://").rstrip("/")
        self.urls=[]
    def run(self):
        with open(self.dirb_temp+"_temp.txt","r") as f:
            with ThreadPoolExecutor(30) as excetor:
                for i in f.readlines():
                    i=i.rstrip("\n")
                    excetor.submit(self.Request,i)
        f.close()
        self.Save_urls()
    def Save_urls(self):
        with open(base_path+self.dirb_temp+".txt","w+") as f:
            for i in self.urls:
                f.write(i)
                f.write("\n")
        f.close()
    def Request(self,catalog):
        temp_url=self.url.rstrip("/")+"/"+catalog
        s=requests.get(url=temp_url)
        if s.status_code != 404 :
            print(temp_url)
            self.urls.append(temp_url)

