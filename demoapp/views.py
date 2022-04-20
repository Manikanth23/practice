from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
    m="<h1>Hai Manikanth Your First Django app</h1>"
    return HttpResponse(m)
def nani(request):
    m="<h1>Hai Manikanth Your Second Django app</h1>"
    return HttpResponse(m)
def mani(request):
    m="<h1>Hai Manikanth Your Third Django app</h1>"
    return HttpResponse(m)