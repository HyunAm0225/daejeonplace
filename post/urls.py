from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import PlaceViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet, basename='places')
router.register(r'reviews', ReviewViewSet, basename='reviews')

app_name = 'post'

urlpatterns = [
    # path('places/',),
    path('', include(router.urls))
]
