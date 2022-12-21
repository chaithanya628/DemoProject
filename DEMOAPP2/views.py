from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def f3(request):
    return HttpResponse("<h1>Hello from DEMOAPP2 f3()</h1><hr/>");

def f4(request):
    return HttpResponse("<h5>Hello from DEMOAPP2 f4()</h5><hr/>");
