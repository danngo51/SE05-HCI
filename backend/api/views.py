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