# web_deal_scripts  
下载链接：https://github.com/nihaohello/web_deal_scripts

这几个脚本的目的：  
主要是有一些工作太繁琐重复，就写点脚本，把前面的一些操作一起做了  
其中Get_Target中个人渗透流程和大纲把思路说了些  


Get_Target目录中的：  
    step1.txt  是漏洞银行列出来的target网址  
    漏洞银行目标选取.py   是随机选取一个step1.txt的网址（毕竟自己多了，选择起来就麻烦了）  
    选取目标的某个子域名.py    也是一个选取网址的脚本  



0.用whatweb.py是一个处理whatweb中不合格的网址  
1.先用一些子域名收集器收集一些子域名，保存在urls.txt  
2.然后用whatweb工具进行筛选：whatweb -i urls.txt | sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g" | tee whatweb_urls.txt  
3.dirb_scan_from_whatweb.py  提取http://www.baidu.com这样的网址出来，保存到dirb_urls.txt中  
4.用dirb_scan.py进行扫描（其中，个人只收集了4700个在dirb_wordlist.txt中），将结果保存在diab_catlog目录里  
其中dirb_scan.py是调用dirb进行扫描  
dirb_scan2.py是个人写的脚本进行扫描目录  
5.用get_nmap_from_whatweb.py   取得nmap要扫描的ip地址，保存到nmap_ips.txt中  
6.然后用：  
nmap -sV -Pn -v ip,ip,ip  
nikto -h ip  
参考：https://www.cnblogs.com/weihua2616/p/6599629.html  
nmap -sS -F -T4 -v -iL nmap_ips.txt | tee nmap_results.txt   -F是只扫描100个端口  
nmap -sS -T4 -v --script=vuln -iL nmap_ips.txt | tee nmap_results.txt  
7.
用IIS_Apache_Nginx_classify进行处理whatweb结果进行分类，分成apache和iis，nginx  
iis，就继续用asp下工具的进行探测  
apache再看语言，jsp，php进行等等等操作  




后面的看自己了，个人仅仅只是觉得前面的操作很繁琐但是又不得不做，所以花时间写了脚本处理  

2019.3.5  
------------------------------------
添加了dirb_scan2.py,完善了简单的dirb目录扫描  

2019.3.6