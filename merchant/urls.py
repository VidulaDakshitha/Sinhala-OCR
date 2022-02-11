from django.conf.urls import url
from rest_framework import routers
from .views import *

urlpatterns=[
    url(r"^register", MerchantSelfRegisterView.as_view(), name="template identification")
]