from django.db import models

# Create your models here.

class Customerdetails(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    password  = models.CharField(max_length=100,null=True,blank=True)
    confirmpassword = models.CharField(max_length=100,null=True,blank=True)


class Cart(models.Model):
    product = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)


