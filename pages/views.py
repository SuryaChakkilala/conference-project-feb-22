from django.shortcuts import render
from .models import *

# Create your views here.

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
