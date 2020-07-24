from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserCreate
def register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print("User Created")
        return render(request, 'login.html')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,'home.html')
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')