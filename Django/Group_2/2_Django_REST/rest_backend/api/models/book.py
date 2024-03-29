from django.db import models
from . import Author


class Book(models.Model):
    """
    Book model

    Attributes:
        title (CharField)
        author_id (ForeignKey)
    """
    title = models.CharField(max_length=150)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
