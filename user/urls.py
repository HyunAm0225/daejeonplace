from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('current/', views.CurrentUserView.as_view(), name='info'),
]
