from django.db import models

from merchant.models import Merchant
from user.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Template(models.Model):
    user = models.ForeignKey(User,related_name="templ_user",on_delete=models.CASCADE,default=None)
    merchant = models.ForeignKey(Merchant,related_name="temp_mer_user",on_delete=models.CASCADE,default=None)
    image_url=models.CharField(_('image_url'),max_length=1000,null=True,blank=True)
    questions=models.CharField(_('questions'),max_length=100,null=True,blank=True)
    name = models.CharField(_('name'),max_length=100,null=True,blank=True)

class Answer(models.Model):
    user = models.ForeignKey(User, related_name="ans_user", on_delete=models.CASCADE, default=None)
    template = models.ForeignKey(Template,related_name="temp_mer",on_delete=models.CASCADE,default=None)
    ans_string = models.CharField(_('ans_string'),max_length=1000,null=True,blank=True)