from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from matplotlib.style import use
from django.contrib.auth import logout, authenticate, login
# from django.contrib.auth import authenticate
# username swaraj
# password for test user is swaraj754132
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        # chake if user has entered correct credentials
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
    
