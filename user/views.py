from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SignupSerializer
from .models import User
from rest_framework.generics import CreateAPIView
# Create your views here.


class SignupView(CreateAPIView):
    model = User
    serializer_class = SignupSerializer
    Permission_classes = [
        AllowAny
    ]
