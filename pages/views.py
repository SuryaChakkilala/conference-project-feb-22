from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from .forms import RegiserUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def registerPage(request):
    form = RegiserUserForm()
    if request.method == "POST":
        form = RegiserUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect('login')
        
    context = {'form': form}
    return render(request, 'pages/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username (or) Password is incorrect')
            
    context = {}
    return render(request, 'pages/login.html', context)

def home(request):
    context = {}
    return render(request, 'pages/home.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)

def conferences(request):
    events_list = Conference.objects.all()
    context = {'events_list': events_list}
    return render(request, 'pages/conferences.html', context)

def paper_presentations(request):
    events_list = PaperPresentation.objects.all()
    context = {'events_list': events_list}
    return render(request, 'pages/paper_presentations.html', context)