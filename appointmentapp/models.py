from django.db import models
from django import forms 
import datetime as dt 

class Appointment(models.Model):
    appointment_number=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    contact=models.CharField(max_length=20)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
 
    class Meta:
        db_table='appointment'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['appointment_number','name','contact','appointment_date','appointment_time']
