from django import views  
from django.urls import path, include
from .views import  acceuil, service, aboutus

urlpatterns = [
    path('', acceuil, name='acceuil'),
    path('service.html/', service, name='service'),  
    path('aboutus.html/', aboutus, name='aboutus'),  

]