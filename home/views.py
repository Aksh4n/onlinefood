from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    return render(request, 'index.html' , {'p':pro , 'c':cat})

def order(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    return render(request, 'order.html' , {'p':pro , 'c':cat})