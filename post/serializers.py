from rest_framework import serializers
from .models import Review, Place
from pathlib import Path

import json
import os
import requests
import time
from django.core.exceptions import ImproperlyConfigured

# # Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')

# 파이썬 비밀코드 관리
with open(secret_file) as f:
    secrets = json.loads(f.read())


def address_to_latlon(address):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(
        address)
    headers = {
        "Authorization": f"KakaoAK {KAKAO_KEY}"
    }
    result = requests.get(url, headers=headers).json()['documents']
    # print(result)
    # json_obj = result.json()
    for document in result:
        val = [
            document['address_name'], document['x'], document['y']]
    # val = [result['address_name'], result['x'], result['y']]
    return val


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


KAKAO_KEY = get_secret("rest_api_key")


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'address',)
        # fields = '__all__'

    def create(self, validated_data):
        find_address_result = address_to_latlon(validated_data['name'])
        place = Place.objects.create(name=validated_data['name'], description=validated_data['description'],
                                     address=find_address_result[0], latitude=find_address_result[1], longitude=find_address_result[2])
        place.save()
        return place


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'comment', 'stars', 'writer', 'place',)
        # fields = '__all__'
