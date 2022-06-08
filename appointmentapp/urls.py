
from django.urls import path
from .import views as v 

urlpatterns = [
    path('addappointment',v.add_appointment,name="addappointment"),
    path('appointmentapp-list',v.appointmentapp_list,name="appointmentapplist"),
    path('delete/<int:id>',v.delete_appointment,name="deleteappointment"),
    path('edit/<int:id>',v.edit_appointment,name="editappointment"),
]
