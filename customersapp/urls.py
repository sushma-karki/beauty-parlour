from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('addcustomers',v.add_customers,name='addcustomers'),
    path('customers-list',v.customers_list,name='customerslist'),
    path('delete/<int:id>',v.delete_customers,name="deletecustomers"),
    path('edit/<int:id>',v.edit_customers,name="editcustomers"),
]
