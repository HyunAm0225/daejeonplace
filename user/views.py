from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SignupSerializer
from .models import User
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class SignupView(CreateAPIView):
    model = User
    serializer_class = SignupSerializer
    Permission_classes = [
        AllowAny
    ]


class CurrentUserView(APIView):
    def get(self, request):
        serializer = SignupSerializer(request.user)
        return Response(serializer.data)
