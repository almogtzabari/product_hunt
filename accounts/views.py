from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    # Check if user is trying to sign up
    if request.method == 'POST':
        username = request.POST['username']
        pw1 = request.POST['password1']
        pw2 = request.POST['password2']
        # Check if passwords match
        if pw1 == pw2:
            # Check if user already exists
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=pw1)
                auth.login(request, user)
                return redirect('home')
            return render(request, 'accounts/signup.html', {'error': f'Username "{username}" has already been taken!'})

        else:
            # Passwords does not match
            return render(request, 'accounts/signup.html', {'error': 'Passwords does not match!'})

    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            # Incorrect username or password
            return render(request, 'accounts/login.html', {'error': 'Username and/or password are incorrect!'})

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')



