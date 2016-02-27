###This is a repo use Django+bootstrap+d3.js for rank github user/repo and recommended repo/language, fork by edx_analytics_ustc.Base on open edx platform.
###Analysis tracking log to recommended github repo,and use fp-tree to find frequent pattern,knn algorithm to find what determine the high grade.
####Get start to use display.py file with commend
```
cd RecGithub/function
python start_service.py 8989
```
####Then,type commend python or ipython notebook,
```
import display as da
da.knn()
da.githubRec()
da.fptree()
da.svd()
```
###Write your github username,password in config.cfg(a new file in RecGithub make yourself) as follow:
```
[info]
user:xxxxxxx
passwd:xxxxx
```
###Get Web service start:
```
python manage.py runserver 0.0.0.0:8000
```
###And then,open your browser with address of 127.0.0.1:8000

###Your might install numpy,networkx,pygithub,pandas,ipython-notebook,d3py tools first when you attemp modify some files and compile it.
##Author by ch yy in SuZhou.
##USTC SSE 
##Contact me by eamil ch710798472@gmail.com

