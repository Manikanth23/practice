from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('demo',demo),
    path('nani',nani),
    path('mani',mani),   
]