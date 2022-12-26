from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    # id = will be created automatically
    # password
    # last_login
    email = models.EmailField("email_address", unique=True, null=True)
    first_name = models.CharField("first_name", max_length=35, null=True)
    last_name = models.CharField("last_name", max_length=35)
    is_active = models.BooleanField("active", default=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
