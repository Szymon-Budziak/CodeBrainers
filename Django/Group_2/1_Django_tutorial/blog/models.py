from django.db import models
from django.utils import timezone
from django.conf import settings


# Django model == SQL table
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()  # save to database

    def __str__(self):
        return f"Post with title {self.title} created by {self.author}"
