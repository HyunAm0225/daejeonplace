from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

# from user.views import UserViewSet

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('users/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
