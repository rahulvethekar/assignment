from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from .models import Post

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        