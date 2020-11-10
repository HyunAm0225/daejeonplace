from django.shortcuts import render
from rest_framework import viewsets
from .models import Place, Review
from .serializers import PlaceSerializer, ReviewSerializer
# # Create your views here.


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
