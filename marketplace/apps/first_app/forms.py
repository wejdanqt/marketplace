from django import forms 
from .models import *

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