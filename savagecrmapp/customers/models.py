import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class   Customer(models.Model):
    c_name = models.CharField(max_length=200)
    c_lastname = models.CharField(max_length=200)
    c_phone = models.CharField(max_length=50)
    c_nick_name = models.CharField(max_length=200)
    c_password = models.CharField(max_length=200)
    reg_date = models.DateTimeField("Date Registered")
    
    def __str__ (self):
        return self.c_name+' '+self.c_lastname

    def reg_recently(self):
        return self.reg_date >= timezone.now()- datetime.timedelta(months=1)

class Service(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    service= models.CharField(max_length=50)
    drink= models.CharField(max_length=50)
    product_bought= models.CharField(max_length=100)
    product_used= models.CharField(max_length=100)
    payment_way=models.CharField(max_length=100)
    bougth_date= models.DateTimeField("Bougth Date")
    times= models.IntegerField(default=0)
    
    def __str__ (self):
        return self.service

    def buy_recently(self):
        return self.reg_date >= timezone.now()- datetime.timedelta(months=1)