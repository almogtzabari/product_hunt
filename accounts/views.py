from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    # User is trying to sign up
    if request.method == 'POST':

        # Check if passwords match
        if request.POST['password1'] == request.POST['password2']:

            # Check if user already exists
            try:
                user = User.objects.get(username=request.POST['username'])
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')

            return render(request, 'accounts/signup.html', {'error': 'Username has already been taken!'})

        else:
            # Passwords does not match
            return render(request, 'accounts/signup.html', {'error': 'Passwords does not match!'})

    return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    pass


