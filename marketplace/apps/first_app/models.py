from django.db import models
    
class Product(models.Model):
    name = models.CharField(max_length=45 , null=False )
    headline = models.CharField(max_length=300,  null=False )
    description =  models.CharField(max_length=700 ,  null=False )
    photo = models.ImageField(upload_to='images/' , blank=False)

    