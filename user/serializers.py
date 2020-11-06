# from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password',
                  'username', 'gender',)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user
