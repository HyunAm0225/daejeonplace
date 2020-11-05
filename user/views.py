from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
