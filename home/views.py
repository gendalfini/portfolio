from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from random import choice



def home(request):
    parts = Project.objects.all()
    return render(request, 'home.html', {'parts':parts})

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')
