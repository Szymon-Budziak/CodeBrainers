from django.db import models

from . import Author


class Book(models.Model):
    """
    Book model

    Attributes:
        title (CharField): title of book
        author_id (ForeignKey): foreign key to Author model
    """
    title = models.CharField(max_length=128)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
