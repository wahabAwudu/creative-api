from django.db import models
from django.conf import settings

class Key(models.Model):
    text = models.CharField(max_length=50, unique=True)
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.text)
