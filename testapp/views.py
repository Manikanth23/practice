from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def mani(request):
    date=datetime.datetime.now()
    name="Mani"
    age=27
    # my_dict={'date':date}
    # return render(request,'testapp/home.html',context=my_dict)   #this is also works
    return render(request,'testapp/home.html',{'date':date,'name':name,'age':age})  #directly we can pass dictionary also and we can pass any no.of key values.......

def morning(request):
    m="<h1>Hai Mani Good Morning</h1>"
    return HttpResponse(m)

def afternoon(request):
    m="<h1>Hai Mani Good Afternoon</h1>"
    return HttpResponse(m)
def evening(request):
    m="<h1>Hai Mani Good Evening</h1>"
    return HttpResponse(m)
def night(request):
    m="<h1>Hai Mani Good night</h1>"
    return HttpResponse(m)
