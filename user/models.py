from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True,null=True)
    phone_no = models.CharField(_('phone number'),max_length=15,unique=True,null=True)
    last_login = models.CharField(_('last login'),max_length=100,unique=True,null=True)
    date_joined = models.CharField(_('date_joined'),max_length=200,null=True)
    is_active = models.BooleanField(_('active'),default=True)
    is_verified = models.BooleanField(_('active'),default=False)
    is_merchant = models.BooleanField(_('is_merchant'),default=False)
    is_user = models.BooleanField(_('is_user'),default=False)
    login_attempts = models.CharField(_('login_attempts'),max_length=30,blank=True,null=True)
    is_delete = models.BooleanField(_('is_delete'),default=False)
    delete_on = models.CharField(_('delete_on'),max_length=200,blank=True,null=True)
    reset_token = models.CharField(_('reset_token'),max_length=200,blank=True,null=True)
    reset_token_expire_date = models.CharField(_('reset_token_expire_date'),max_length=200,blank=True,null=True)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []

class PasswordHistory(models.Model):
    user = models.ForeignKey(User,related_name="user_password_history",on_delete=models.CASCADE,null=True,blank=True)
    create_on = models.CharField(_('create_on'),max_length=200,null=True,blank=True)
    password = models.CharField(_('password'),max_length=250,null=True,blank=True)