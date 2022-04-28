from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.


class MainProfile(AbstractUser):
    email = models.EmailField(_('email_address'), max_length=70, blank=True, null=True, unique=True)
    image = models.ImageField(default='default.jpg', upload_to='accounts', null=True)
    favourite_brand = models.CharField(max_length=40, null=True, blank=True)
