from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home',mani),
    path('m',morning),
    path('a',afternoon),
    path('e',evening),
    path('n',night),

]
