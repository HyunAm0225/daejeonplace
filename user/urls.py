from django.urls import path

from . import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

app_name = 'user'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('current/', views.CurrentUserView.as_view(), name='info'),
    path('update/', views.UpdateName.as_view(), name='update_name'),
    path('pwchange/', views.UpdatePassword.as_view(), name='change_pw'),

    path('token/', obtain_jwt_token),
    path('token/refresh', refresh_jwt_token),
    path('token/verify', verify_jwt_token),
]
