from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def f1(request):
    return HttpResponse("<h3>Hello from DEMOAPP1 f1()</h3><hr/>");

def f2(request):
    return HttpResponse("<h2>Hello from DEMOAPP1 f2()</h2><hr/>");
