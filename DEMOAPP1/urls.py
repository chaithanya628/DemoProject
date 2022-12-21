from django.urls import path;
from DEMOAPP1 import views;

urlpatterns = [
    path('first/',views.f1),
    path('second/',views.f2),
];