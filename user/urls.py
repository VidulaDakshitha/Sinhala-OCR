from django.conf.urls import url
from rest_framework import routers
from .views import *

urlpatterns=[
    url(r"^login", LoginView.as_view(), name="user login"),
    url(r"^verify", ResetPassword.as_view(), name="reset password")
]