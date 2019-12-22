from django import forms 
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.core import validators

class addform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name' , 'headline' , 'description', 'photo']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': 'form-control' , 
                'placeholder':"Product Name",
                'onfocus':"this.placeholder : ''",
                'onblur':"this.placeholder : 'Product Name'",
                'size': 20
            }) ,

            'headline' : forms.TextInput(attrs={
                'class': 'form-control' , 
                'placeholder':"Headline",
                'onfocus':"this.placeholder : ''",
                'onblur':"this.placeholder : 'Headline'",
            } ), 
             'description' : forms.Textarea(attrs={
                'class':"form-control mb-10" , 
                'placeholder':"Description",
                'onfocus':"this.placeholder : ''",
                'onblur':"this.placeholder : 'Description'",
                'cols': 10, 
                'rows': 20

            } ), 
        }
        labels = {
            "name":'',
            "headline":'',
            'description' : ''

        }

class UserForm(forms.ModelForm):
    # password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password])

    password = forms.CharField( validators=[validate_password] , widget=forms.PasswordInput(attrs={
                'class': 'form-control' , 
                'placeholder':"Password",
                'onfocus':"this.placeholder : ''",
                'onblur':"this.placeholder : 'Password'",

            } ) , label= '')

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control' , 
                'placeholder':"Confirm Password",
                'onfocus':"this.placeholder : ''",
                'onblur':"this.placeholder : 'Confirm Password'",

            } ) , label= '')

    class Meta:
        model = User
        fields = ['username','email','password' , 'confirm_password']
    
        widgets = {
            'username' : forms.TextInput(attrs={
                'class': 'form-control' , 
                'placeholder':"Username",
                'onfocus':"this.placeholder : ''",
                'onblur':"this.placeholder : 'Username'",
    
            }) ,

            'email' : forms.TextInput(attrs={
                'class': 'form-control' , 
                'placeholder':"Email",
                'onfocus':"this.placeholder : ''",
                'onblur':"this.placeholder : 'Email'",
            } ), 
             'password' : forms.PasswordInput (attrs={
                'class': 'form-control' , 
                'placeholder':"Password",
                'onfocus':"this.placeholder : ''",
                'onblur':"this.placeholder : 'Password'",

            } ), 
            

        }
        labels = {
            "username":'',
            "email":'',
            'password' : '',
        }
        validators = {
             'password' : [validate_password]
        }
    


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control' , 
                'placeholder':"Username",
                'onfocus':"this.placeholder : ''",
                'onblur':"this.placeholder : 'Username'",
        } ) , label= '')

    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control' , 
                'placeholder':"Password",
                'onfocus':"this.placeholder : ''",
                'onblur':"this.placeholder : 'Password'",

            } ) , label= '')




        
