from django import views 
from django.urls import path,include
from .views import*

urlpatterns = [
    path('',acceuil,name="acceuil"),
    path('Login.html/',Login,name="Login"),
    path('register.html/',register,name="register"),
    path('aboutus.html/',aboutus,name="aboutus"),
    path('reserver.html/',reserver,name="reserver"),
    
  
]
