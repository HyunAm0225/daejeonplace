from rest_framework import serializers
from .models import Review, Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'address',)
        # fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'comment', 'stars', 'writer', 'place',)
        # fields = '__all__'
