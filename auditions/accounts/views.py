from django.forms.widgets import PasswordInput
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate,logout
from .forms import RegisterForm
from .models import Profile

# Create your views here.

def index(request):
    return render(request,'accounts/index.html')


def registerview(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            profile = Profile(user = user)
            profile.save()
            return redirect('login')
    else:
        form = RegisterForm()
        return render(request, 'accounts/signup.html', {'form': form})

def loginview(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if(user is not None):
            if(user.is_active):
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse('user Inactive')
        else:
            return HttpResponse('Login Unsuccessful')
    else:
        return render(request,'accounts/login.html')

def logoutview(request):
    logout(request)
    return redirect('login')