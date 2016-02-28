"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from RecGithub import views

urlpatterns = [
    url(r'^form/$',views.form,name='form'),
    url(r'^repo/$',views.repo,name='repo'),
    url(r'^connect/$',views.connect,name='connect'),
    url(r'^add/(\d+)/(\d+)/$', views.add, name='add'),
    url(r'^search/$', views.search,name='search'),
    url(r'^nonconnect/$', views.nonconnect,name='nonconnect'),
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='home'),
]
