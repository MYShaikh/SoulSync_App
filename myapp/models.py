from django.db import models

# Create your models here.
class Books(models.Model):
    name= models.CharField(max_length=50, null=True, blank=True)
    author =models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField()

class Ouruser(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, unique= True)
    message = models.TextField(null=True, blank=True)
    createdDate = models.DateField(auto_now=True)
    createdTime = models.TimeField(auto_now=True)

class Product(models.Model):
    product_name =models.CharField(max_length=50, null=True, blank=True)
    product_model =models.CharField(max_length=50, null=True, blank=True)
    product_price =models.IntegerField(null=True,blank=True)
    product_desc = models.TextField(null=True,blank=True)
    Product_image = models.ImageField(null=True,upload_to="Images")

class RegisteredUsers(models.Model):
    user_name = models.CharField(max_length=50, null=True, blank=True)
    user_email = models.EmailField(max_length=50, unique= True)
    user_password = models.CharField(max_length=150, null=True, blank=True)
