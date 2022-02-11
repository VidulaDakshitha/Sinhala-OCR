from django.conf.urls import url
from rest_framework import routers
from .views import *

urlpatterns=[
    url(r"^template$", questionOcrIdentification.as_view(), name="template identification"),
    url(r"^answer", answerOcrIdentification.as_view(), name="answer identification"),
    url(r"^custom", answerOcrIdentificationCustom.as_view(), name="answer identification"),
    url(r"^grammar", grammarDetection.as_view(), name="grammar detection"),
    url(r"^get_template", TemplateData.as_view(), name="get template"),
    url(r"^template-ans", trainAnswer.as_view(), name="answer save"),

]