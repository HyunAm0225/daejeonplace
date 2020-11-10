from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', include('user.urls', namespace='users')),
    path('post/', include('post.urls', namespace='posts')),

]
