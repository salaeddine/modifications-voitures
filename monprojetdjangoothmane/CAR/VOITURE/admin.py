from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class userAdmin(admin.ModelAdmin):
    list_display = ('id','nom','prenom','email','mot_de_passe')
    
