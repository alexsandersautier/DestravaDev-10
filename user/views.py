from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib import messages


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        user = request.POST['user']
        password = request.POST['password']

        userDb = authenticate(username=user, password=password)

        if userDb:
            login_django(request, userDb)
            return redirect("tasks")
        else:
            return HttpResponse("Usuário ou senha inválidos verifique")
        
def register(request):
    if request.method == 'GET':
        return render(request, "register.html")
    else:
        user = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')

        userDb = User.objects.filter(username=user).first()

        if userDb:
            return HttpResponse(f"Usuário {userDb} já registrado")
        
        newUser = User.objects.create_user(username=user, email=email, password=password)
        newUser.save()
        return redirect("login")
    
def logout(request):
    logout_django(request)
    return redirect('login')