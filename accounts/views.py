from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST["user"], password=request.POST["password"])
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {"error": 'Il n\'y a pas de compte avec ces informations! Veuillez réessayer'})
    else:
        return render(request, 'accounts/login.html')

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.get(username=request.POST["user"])
                return render(request, 'accounts/signup.html', {"error": "Ce nom d'utilisateur a déjà été utilisé pour ouvrir un compte!"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST["user"], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {"error": "Les deux mots de passe sont différents !"})
    else:
        return render(request, 'accounts/signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
