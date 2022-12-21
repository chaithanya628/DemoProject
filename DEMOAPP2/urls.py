from django.urls import path;
from DEMOAPP2 import views;

urlpatterns = [
    path('third/',views.f3),
    path('fourth/',views.f4),
];