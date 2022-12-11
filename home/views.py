from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request, 'index.html' , {})

def order(request):
    return render(request, 'order.html' , {})