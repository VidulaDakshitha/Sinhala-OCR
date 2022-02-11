from django.db import models
from user.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Merchant(models.Model):
    user = models.OneToOneField(User,related_name="mer_user",on_delete=models.CASCADE,null=True,blank=True)
    first_name=models.CharField(_('first_name'),max_length=100,null=True,blank=True)
    last_name=models.CharField(_('last_name'),max_length=100,null=True,blank=True)
    business_category = models.CharField(_('business_catergory'), max_length=100, null=True, blank=True)
    trading_name = models.CharField(_('trading_name'), max_length=100, null=True, blank=True)
