#####This repo use Django+bootstrap+d3.js to rank github user/repo and recommended repo/language, forked by edx_analytics_ustc.

###Getting start by dev-environment:

####1.Write your github username,password in config.cfg(a new file in RecGithub make yourself) as follow:
```
[info]
user:xxxxxxx
passwd:xxxxx
```
####2.Get Web service start:
```
python manage.py runserver 0.0.0.0:8000
```
####3.And then,open your browser with address of 127.0.0.1:8000

###Deploy on your server:[see my blog](http://ch710798472.github.io/blog/java/2016/05/02/tx.html),see the result in [my web server](http://115.159.187.117)

####Notes: Your might install numpy,networkx,pygithub,pandas,ipython-notebook,d3py tools first when you attemp modify some files and compile it.
Author by ch and yy in SuZhou,USTC SSE.
Contact me by eamil ch710798472@gmail.com

