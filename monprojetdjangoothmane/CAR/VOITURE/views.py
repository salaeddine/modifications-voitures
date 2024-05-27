from django.shortcuts import render,redirect
from .forms import UserCreationForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def acceuil(request):
    return render(request,'acceuil.html')

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirigez l'utilisateur vers une page appropriée après la connexion
                return redirect('acceuil')  
            else:
                # Afficher un message d'erreur si l'authentification échoue
                messages.error(request, "L'adresse e-mail ou le mot de passe est incorrect.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('acceuil') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def aboutus(request):
    return render(request,'aboutus.html')

def reserver(request):
    return render(request,'reserver.html')




