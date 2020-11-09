from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from user.models import User
# Create your models here.


class Place(models.Model):
    name = models.CharField('장소명', max_length=50)
    latitude = models.FloatField(
        '위도', validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(
        '경도', validators=[MinValueValidator(-180), MaxValueValidator(180)])
    address = models.CharField('주소', max_length=100)
    description = models.TextField('설명', blank=True)

    def avg_rating(self):
        sum = 0
        ratings = Review.object.filter(place=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0


class Review(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    comment = models.CharField('한줄 평', max_length=200)
    stars = models.FloatField(
        '평점', validators=[MinValueValidator(1), MaxValueValidator(5)])
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자', blank=True, null=True)
    registered_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')
