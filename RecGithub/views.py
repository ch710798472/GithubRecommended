#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# 引入我们创建的表单类
from models import SearchForm
import requests

def index(request):
    return render(request, 'index.html')
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
def home(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'TutorialList': TutorialList})
def home1(request):
    List = map(str, range(100))# 一个长度为100的 List


def form(request):
    if request.method == 'POST':# 当提交表单时

        form = SearchForm(request.POST) # form 包含提交的数据

        if form.is_valid():# 如果提交的数据合法
            location = form.cleaned_data['location']
            language = form.cleaned_data['language']

            return HttpResponse(str(GetUser(location,language)))

    else:# 当正常访问时
        form = SearchForm()
    return render(request, 'home.html', {'form': form})

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