#coding:utf-8
from django.shortcuts import render
from github import Github
import json
# Create your views here.
from django.http import HttpResponse
# 引入我们创建的表单类
from models import SearchForm
import requests

def index(request):
    return render(request, 'index.html')
def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
def home(request):
    return render(request, 'index.html')

def form(request):
    if request.method == 'POST':# 当提交表单时

        form = SearchForm(request.POST) # form 包含提交的数据

        if form.is_valid():# 如果提交的数据合法
            location = form.cleaned_data['location']
            language = form.cleaned_data['language']

            if GetSearchInfo(location,language):
                return render(request,'search_result.html')
            else:
                return HttpResponse(str("查找结果不存在，请重新输入！"))

    else:# 当正常访问时
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

def GetUser(location,language):
    d = {"items":[]}
    url = 'https://api.github.com/search/users?sort=followers&q=location:%s+language:%s&per_page=100&page=' % (location,language)
    rank_count=1
    for i in range(rank_count):
        print url + str(i+1)
        newUrl = url + str(i+1)
        r = requests.get(newUrl)
        temp = r.json()
        d['items'].extend(temp['items'])
    return d

def GetSearchInfo(location,language):
    #search 100 users from location,language
    d = {"items":[]}
    url = 'https://api.github.com/search/users?sort=followers&q=location:%s+language:%s&per_page=100&page=' % (location,language)
    rank_count=1

    #获取排名
    for i in range(rank_count):
        print url + str(i+1)
        newUrl = url + str(i+1)
        r = requests.get(newUrl)
        temp = r.json()
        d['items'].extend(temp['items'])

    print 'GetSearchInfo->finish rank user'

    #获取用户详细信息
    username = 'ch710798472'
    password = 'Mm456123'
    ACCESS_TOKEN = '0d1c6d6da836bc28b691f87dd34a1fbdc604c895'
    client = Github(username,password=password, per_page=100)
    t = {}
    notdone=[]
    j=0
    for i in d['items']:
        try:
            user = client.get_user(i['login'])
            t[user._rawData['login']] = user._rawData
        except Exception,e:
            print "GetSearchInfo->time out"
            notdone.append(i['login'])
        if (j%10)==0:
            print j
        j = j + 1

    print 'GetSearchInfo->finish user info'

    #重新排序

    d1 = []#最后的结果存储
    for i in d['items']:
        for k in t:
            try:
                if i['login'] == k:
#                   print k
                    d1.append(t[k])
#                   apendx.append(k)
            except Exception,e:
                pass

    print 'GetSearchInfo->DONE'

    if len(d1):
        # filename=+ location+ '_'+language+ '.json'
        filename='./static/bootstrap/data/search.json'
        json.dump(d1, open(filename, 'w'))
        return 1
    else:
        return 0

def search(request):
    searchKey = request.GET['searchKey']
    if searchKey.strip()=='':
         return HttpResponse(str("请输入查找关键字！"))
    else:
        return HttpResponse(str(searchKey))