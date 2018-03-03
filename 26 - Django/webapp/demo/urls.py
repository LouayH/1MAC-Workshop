from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('SayHello/<name>', views.say_hello),
]