from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage),
    path('register/', views.register),
    path('logIn/', views.logIn),
    path('personalization', views.personalization),
    path('home/', views.home),
    path('home/preferences/', views.preferences),
    path('home/recipe/', views.recipe),
    path('home/mypage/', views.mypage),
]