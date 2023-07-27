from django.db import models
from django.contrib.auth.models import User
import secrets


class ActionAuthorization(models.Model):
    key = models.CharField(max_length=64)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=False, auto_now=True)
    info = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.key = secrets.token_urlsafe(32)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.key
