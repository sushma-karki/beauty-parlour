from django.db import models      
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields     

class UserInfo(User):
    contact=models.CharField(max_length=15)
    address=models.TextField(max_length=300)

    class Meta:
        db_table="userinfo"
         
class UserForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','first_name','last_name','email','contact','address','password1','password2']


from django import forms 
class LoginForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','password1','password2']




