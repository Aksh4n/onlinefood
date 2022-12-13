from django.shortcuts import render
from django.http import JsonResponse
from .forms import *
from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
import json
# Create your views here.
from django.template import RequestContext
# Create your views here.
from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    return render(request, 'index.html' , {'p':pro , 'c':cat,'room_name': "broadcast"})

def order(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    sos = Sauce.objects.all()
    dri = Drink.objects.all()
    return render(request, 'order.html' , {'p':pro , 'c':cat,'s':sos, 'd':dri})
def orderb(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    sos = Sauce.objects.all()
    dri = Drink.objects.all()
    return render(request, 'orderb.html' , {'p':pro , 'c':cat,'s':sos, 'd':dri})



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




from asgiref.sync import async_to_sync
def test(request):
    
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': json.dumps("Notification")
        }
    )
    return HttpResponse("Done")