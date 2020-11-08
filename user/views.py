from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import SignupSerializer, ChangePasswordSerializer
from .models import User
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.


class SignupView(CreateAPIView):
    model = User
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny
    ]


class CurrentUserView(APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        serializer = SignupSerializer(request.user)
        return Response(serializer.data)

# 유저 비밀번호 변경


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
