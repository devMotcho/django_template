from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('app:home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, 'Username Not Found!')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome! user.username')
            return redirect('app:home')
        else:
            messages.warning(request, 'Wrong Password!')

    return render(request, 'app/login.html')


def logoutUser(request):
    logout(request)
    return redirect('app:login')