from django.shortcuts import render
from .models import *


def home(request):
    data = {'posts': Post.objects.all()}
    return render(request, 'app/home.html', data)


def about(request):
    return render(request, 'app/about.html', {'title': 'About'})



