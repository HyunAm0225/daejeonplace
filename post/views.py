from django.shortcuts import render
from urllib.parse import urlparse
from rest_framework import viewsets
from .models import Place, Review
from rest_framework.response import Response
from .serializers import PlaceSerializer, ReviewSerializer
from django.core.exceptions import ImproperlyConfigured


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
