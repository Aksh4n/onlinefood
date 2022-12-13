from django.shortcuts import render
from django.http import JsonResponse
from .forms import *
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
def orderb(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    return render(request, 'orderb.html' , {'p':pro , 'c':cat})



def contact(request):
       


    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()
                
            return JsonResponse({
                'msg': 'Success'
                })

def order1(request):
       


    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid() :
            form.save()
                
            return JsonResponse({
                'msg': 'Success'
                })    
        else :
            return JsonResponse({
                'msg': 'failed'
                })    
def order2(request):
       


    if request.method == "POST":
        form = OrderForm2(request.POST)
        if form.is_valid() :
            form.save()
                
            return JsonResponse({
                'msg': 'Success'
                })    
        else :
            return JsonResponse({
                'msg': 'failed'
                })    
