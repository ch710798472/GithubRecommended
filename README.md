# edx_analytics_ustc
###Base on open edx platform.
###Analysis tracking log to recommended github repo,and use fp-tree to find frequent pattern,knn algorithm to find what determine the high grade.
####Get start to use display.py file with commend
```
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
###Get bootstrap webpage start with
```
python3 -m http.server 8001
```
###And then,open your browser with address of 127.0.0.1:8001

###Your might install numpy,networkx,github,pandas,ipython-notebook,d3py tools first.
##Author by ch yy in SuZhou.
##USTC SSE

