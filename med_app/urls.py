from django.urls import re_path

from .view import RegistrationAPIView, LoginAPIView, UserAPIView, UserProfileAPIView

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    re_path(r'^users/?$', UserAPIView.as_view(), name='users'),
    re_path(r'^profile/?$', UserProfileAPIView.as_view(), name='user_profile'),
]
