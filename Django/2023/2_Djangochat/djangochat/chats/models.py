from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    chat = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.chat


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return self.content
