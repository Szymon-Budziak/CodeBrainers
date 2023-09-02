from django.db import models


class Author(models.Model):
    """
    Author model

    Attributes:
        first_name (CharField): first name of author
        last_name (CharField): last name of author
    """
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
