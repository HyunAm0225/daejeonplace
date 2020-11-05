from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    CHOICES_GENDER = (
        (GENDER_MALE, '남성'),
        (GENDER_FEMALE, '여성'),
    )
    gender = models.CharField(max_length=10, choices=CHOICES_GENDER, null=True)
