from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True)
 
    def __str__(self):
        return str(self.username)
