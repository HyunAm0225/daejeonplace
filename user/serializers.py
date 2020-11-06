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
        # user.set_password(validated_date['password'])
        # user.set_last_name(validated_date['last_name'])
        # user.set_first_name(validated_date['first_name'])
        # user.set_gender_name(validated_date['gender_name'])
        user.save()
        return user
