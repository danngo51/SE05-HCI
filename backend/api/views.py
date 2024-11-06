from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer #, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

def frontpage(request):
    return render(request, 'main/frontpage.html')

def register(request):
    return render(request, 'main/register.html')

def logIn(request):
    return render(request, 'main/logIn.html')

def personalization(request):
    return render(request, 'home/~~.html') # 4 html

def home(request):
    return render(request, 'home/home.html')

def preferences(request):
    return render(request, 'home/preferences.html')

def recipe(request):
    return render(request, 'home/recipe.html')

def mypage(request):
    return render(request, 'home/~~.html') # 3 html (preferences.html, profile.html, history.html)