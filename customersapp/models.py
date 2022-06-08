from django.db import models
from django import forms 
import datetime as dt  

class Customers(models.Model):
    date=models.DateField()
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=15)
    email=models.EmailField(max_length=40)
    address=models.TextField(max_length=300)
    referred_by=models.CharField(max_length=30)
    customer_remarks=models.CharField(max_length=20)

    class Meta:
        db_table='customers'


class CustomersForm(forms.ModelForm):
    class Meta:
        model=Customers
        fields='__all__'