from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Post, Comment, UserInfo


class UserFormCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title','text']    

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['author','text']

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['address','img']      

       