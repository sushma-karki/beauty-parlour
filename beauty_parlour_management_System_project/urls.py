
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from adminaccountapp.views import home
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('adminaccountapp-',include(('adminaccountapp.urls','adminaccountapp'),namespace='adminaccountapp')),
    path('appointmentapp-',include(('appointmentapp.urls','appointmentapp'),namespace='appointmentapp')),
    path('customersapp-',include(('customersapp.urls','customersapp'),namespace='customersapp')),
    path('servicapp-',include(('servicapp.urls','servicapp'),namespace='servicapp')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
