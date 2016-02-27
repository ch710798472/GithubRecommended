#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __unicode__(self):
        return self.name

#my search form
class SearchForm(forms.Form):
        location = forms.CharField(max_length=20 ,label='所在地区')
        # mail = forms.EmailField(label='电子邮件')
        # topic = forms.ChoiceField(choices=TOPIC_CHOICES,label='选择评分')
        language = forms.CharField(max_length=100 ,label='编程语言')
        def __unicode__(self):
            return self.name

class SearchRepoForm(forms.Form):
        stars = forms.CharField(max_length=20 ,label='获得星数')
        # mail = forms.EmailField(label='电子邮件')
        # topic = forms.ChoiceField(choices=TOPIC_CHOICES,label='选择评分')
        language = forms.CharField(max_length=100 ,label='编程语言')
        def __unicode__(self):
            return self.name

class ConnectForm(forms.Form):
        user = forms.CharField(max_length=20 ,label='用户名称')
        # mail = forms.EmailField(label='电子邮件')
        # topic = forms.ChoiceField(choices=TOPIC_CHOICES,label='选择评分')
        repo = forms.CharField(max_length=100 ,label='用户仓库')
        def __unicode__(self):
            return self.name