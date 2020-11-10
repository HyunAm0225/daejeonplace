from django.shortcuts import render
from pathlib import Path
from urllib.parse import urlparse
from rest_framework import viewsets
from .models import Place, Review
from rest_framework.response import Response
from .serializers import PlaceSerializer, ReviewSerializer
from django.core.exceptions import ImproperlyConfigured
import json
import os
import requests
# # Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')

# 파이썬 비밀코드 관리
with open(secret_file) as f:
    secrets = json.loads(f.read())


def address_to_latlon(address):
    url = "https://dapi.kakao.com/v2/local/search/address.json?query=" + address
    headers = {
        "Authorization": f"KakaoAK {KAKAO_KEY}"
    }
    result = requests.get(url, headers=headers).json()['documents']
    for document in result:
        val = [document['address_name'], document['x'], document['y']]
    return val


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


KAKAO_KEY = get_secret("rest_api_key")


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer_class = PlaceSerializer(data=data)
        serializer_class.is_valid()
        place = Place.objects.get_or_create(name=data['name'], description=data['description'],
                                            address=address_to_latlon(data['name'])[0], latitude=address_to_latlon(data['name'])[1], longitude=address_to_latlon(data['name'])[2])
        print(serializer_class.data)
        return Response(serializer_class.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
