from django.urls import path
from . import views  # Importez vos vues personnalisées à partir du même répertoire

urlpatterns = [
    path('register.html/', views.register_view, name='register'),
    path('login.html/', views.login_view, name='login'),
]
