#coding:utf-8
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
# 引入我们创建的表单类
from models import SearchForm,SearchRepoForm
import requests
from chgithub import GetSearchInfo,SearchRepo,SocialConnect

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

def repo(request):
    if request.method == 'POST':# 当提交表单时

        form = SearchRepoForm(request.POST) # form 包含提交的数据

        if form.is_valid():# 如果提交的数据合法
            stars = form.cleaned_data['stars']
            language = form.cleaned_data['language']

            if SearchRepo(stars,language):
                return render(request,'repo_result.html')
            else:
                return HttpResponse(str("查找结果不存在，请重新输入！"))

    else:# 当正常访问时
        form = SearchRepoForm()
    return render(request, 'repo.html', {'form': form})

def search(request):
    searchKey = request.GET['searchKey']
    if searchKey.strip()=='':
         return HttpResponse(str("请输入查找关键字！"))
    else:
        tmp1 = searchKey.strip().split('/')
        tmp2 = SocialConnect(tmp1[0],tmp1[1])
        if(tmp2):
            return render(request, 'social_connetc.html')
        else:
            return HttpResponse(str('请重新查找！'))