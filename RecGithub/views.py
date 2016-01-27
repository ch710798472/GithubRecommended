#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# 引入我们创建的表单类
from forms import AddForm

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

        form = AddForm(request.POST) # form 包含提交的数据

        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:# 当正常访问时
        form = AddForm()
    return render(request, 'home.html', {'form': form})