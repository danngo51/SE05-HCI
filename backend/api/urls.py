from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage),
    path('register/', views.register),
    path('logIn/', views.logIn),
]