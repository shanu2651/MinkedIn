from django import forms
from django.contrib.auth.models import User

from .models import *


class regform(forms.Form):
    cname = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)
    phone = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(max_length=12)
    cpassword = forms.CharField(max_length=12)
class logform(forms.Form)  :
    email=forms.EmailField()
    password = forms.CharField(max_length=12)
class upform(forms.Form):
    cname = forms.CharField(max_length=50)
    email = forms.EmailField()
    jtitle = forms.CharField(max_length=25)
    jtype = forms.CharField(max_length=25)
    wtype = forms.CharField(max_length=25)
    exp = forms.CharField(max_length=25)
    qualify = forms.CharField(max_length=70)
class userregform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
class userlogform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=15)
class userprofform(forms.ModelForm):
    class Meta:
        model=userprofmodel
        fields='__all__'
class applyform(forms.Form):
    cname=forms.CharField(max_length=50)
    jobtitle = forms.CharField(max_length=50)
    fname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=30)
    resume = forms.FileField()
class selectform(forms.Form):
    email=forms.EmailField()
    msg=forms.CharField(max_length=100)