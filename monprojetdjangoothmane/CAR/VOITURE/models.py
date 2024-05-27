from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(models.Model):
    email= models.CharField(max_length=100)
    mot_de_passe= models.CharField(max_length=100)
    nom= models.CharField(max_length=70)
    prenom= models.CharField(max_length=70)
    
