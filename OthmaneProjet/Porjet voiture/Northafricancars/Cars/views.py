from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def acceuil(request):
    return render(request,'acceuil.html')

def service(request):
    return render(request,'service.html')

def aboutus(request):
    return render(request,'aboutus.html')

