
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from django import forms 
from django.forms.widgets import PasswordInput, TextInput


from django.forms import ModelForm

from . models import Thought



class ThoughtForm(ModelForm):

    class Meta:

        model = Thought
        fields =['title', 'content',]
        exclude = ['user',]


















class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())