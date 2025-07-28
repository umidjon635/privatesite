from django.shortcuts import render
from .models import HeroSection

def home(request):
    hero = HeroSection.objects.first()
    return render(request, 'home.html', {'hero': hero})

def index(request):
    hero = HeroSection.objects.first()
    return render(request, 'index.html', {'hero': hero})
