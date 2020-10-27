from django.shortcuts import render
from django.http import HttpResponse
from .models import blades

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cutlery_index(request):
    return render(request, 'cutlery/index.html', { 'blades': blades })
