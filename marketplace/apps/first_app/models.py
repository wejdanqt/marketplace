from django.db import models
from django.contrib.auth.models import AbstractUser
    
class Product(models.Model):
    name = models.CharField(max_length=45 , null=False )
    headline = models.CharField(max_length=300,  null=False )
    description =  models.CharField(max_length=700 ,  null=False )
    photo = models.ImageField(upload_to='images/' , blank=False)


class User(AbstractUser):
    username = models.CharField(max_length=45 , null=False , unique=True )
    email = models.EmailField(max_length = 100  , null=False , unique=True ) 
    password = models.CharField(max_length=500 , null=False  )
    last_login = models.CharField(max_length=45)

    