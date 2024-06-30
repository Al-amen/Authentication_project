from django import forms
from login_app import models
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','password']


class UserInfoForm(forms.ModelForm):
    
    class Meta:
        model = models.UserInfo
        fields = ('facebook_url','profile_picture')