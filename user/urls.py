from django.urls import path, include
from rest_framework import routers
from .views import CurrentUserView, ChangePasswordView

from . import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


app_name = 'user'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('<user_id>/profile/', views.CurrentUserView.as_view(), name='info'),
    path('<int:pk>/profile/pw', views.ChangePasswordView.as_view(), name='pwchange'),
    path('token/', obtain_jwt_token),
    path('token/refresh', refresh_jwt_token),
    path('token/verify', verify_jwt_token),
]
