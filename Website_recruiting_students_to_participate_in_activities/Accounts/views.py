from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (authenticate, login as auth_login, logout as auth_logout)
from Accounts.models import *
from .forms import UserStudentrRegistrationForm, UserRegisterPerson_responsible_for_the_projectRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'Accounts/home.html')

# def Register(request):
#     return render(request, 'Accounts/register.html')

def Register(request):
    form = UserStudentrRegistrationForm()
    if request.method == 'POST':
        form = UserStudentrRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            form.save()
            return redirect('login')
    else:
        form = UserStudentrRegistrationForm()

    return render(request, 'Accounts/register.html', {
        'form':form,
        })

def RegisterPerson_responsible_for_the_project(request):
    form = UserRegisterPerson_responsible_for_the_projectRegistrationForm()
    if request.method == 'POST':
        form = UserRegisterPerson_responsible_for_the_projectRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_person_responsible_for_the_project = True
            user.save()
            form.save()
            return redirect('login')
    else:
        form = UserRegisterPerson_responsible_for_the_projectRegistrationForm()

    return render(request, 'Accounts/RegisterPerson_responsible_for_the_project.html', {
        'form':form,
    })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if request.user.is_staff:
                return redirect('home2')
            elif request.user.is_person_responsible_for_the_project:
                return redirect('home')
            elif request.user.is_student:
                return redirect('homeStudent')
            else:
                return redirect('/')
    return render(request, 'Accounts/login.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')