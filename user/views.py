from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import SignupSerializer, UpdateNameSerializer, ChangePasswordSerializer
from .models import User
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class SignupView(CreateAPIView):
    model = User
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny
    ]


class CurrentUserView(APIView):
    def get(self, request):
        serializer = SignupSerializer(request.user)
        return Response(serializer.data)

# 유저 이름 변경


class UpdateName(UpdateAPIView):
    queryset = User.objects.all()

    serializer_class = UpdateNameSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.username = request.data.get("username")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class UpdatePassword(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, querset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # 예전 비밀번호 확인하기
            old_password = serializer.data.get("old_password")
            if not self.object.check(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST
                                )
            # 비밀 번호 셋 하기
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
