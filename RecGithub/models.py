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