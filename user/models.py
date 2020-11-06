from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # email은 중복값이 없어야 합니다.
    email = models.CharField(
        max_length=255,
        unique=True
    )
    username = models.CharField(
        'name', max_length=40, unique=False, default='')
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    CHOICES_GENDER = (
        (GENDER_MALE, '남성'),
        (GENDER_FEMALE, '여성'),
    )
    gender = models.CharField(max_length=10, choices=CHOICES_GENDER, null=True)

    @property
    def name(self):
        return f"{self.last_name} {self.first_name}".strip()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'Users'
