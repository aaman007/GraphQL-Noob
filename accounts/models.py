from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(verbose_name=_('Email'), max_length=255, blank=False)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
