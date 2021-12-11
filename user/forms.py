from django import forms
from django.db import models
from django.forms.fields import ImageField
from django.http import request
from .models import *
# import re
# import pandas as pd
# from django.utils.safestring import mark_safe

class uploadModel(forms.ModelForm):
    modelname = forms.CharField(label="",required=True,
                widget=forms.TextInput(attrs={"placeholder":"Model Name",
                                             "size":"40",
                                             "class":"text"}))
    model_data =  forms.FileField(label="",required=True,
                widget=forms.FileInput(attrs={
                    'type':'file',
                    'class':'file',
                    'name':'file',
                }))
    class Meta:
        model=model_data
        fields=[
            'modelname',
            'model_data']

class testForm(forms.ModelForm):
    image = forms.ImageField(required=True)
   
    class Meta:
        model=testing
        fields=[
            'image',
            ]
