from django.shortcuts import render, redirect
from.forms import UserRegister
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save
            return redirect('login')
    else:
        form = UserRegister
    
    context = {
        'form':form
    }
    
    return render(request, "userreg/register.html", context)

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def userlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # change 'home' to your homepage URL name
    else:
        form = AuthenticationForm()

    return render(request, "userreg/login.html", {"form": form})


def home(request):
    return render(request, 'userreg/home.html')

def userlogout(request):
    logout(request)
    return redirect('login')