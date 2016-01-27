__author__ = 'ch'
from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()