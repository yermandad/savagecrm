from django.db import models

# Create your models here.

class   Customer(models.Model):
    c_name = models.CharField(max_length=200)
    c_lastname = models.CharField(max_length=200)
    c_phone = models.CharField(max_length=50)
    c_nick_name = models.CharField(max_length=200)
    c_password = models.CharField(max_length=200)

class Service(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    service= models.CharField(max_length=50)
    drink= models.CharField(max_length=50)
    product_bought= models.CharField(max_length=100)
    product_used= models.CharField(max_length=100)
    payment_way=models.CharField(max_length=100)


