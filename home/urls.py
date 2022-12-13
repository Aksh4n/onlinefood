from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path('order', views.order , name="order"),
    path('contact', views.contact , name="contact"),
    path('order1', views.order1 , name="order1"),
    path('order2', views.order2 , name="order2"),
    path('orderb', views.orderb , name="orderb"),
    path('test', views.test , name="test"),


]
