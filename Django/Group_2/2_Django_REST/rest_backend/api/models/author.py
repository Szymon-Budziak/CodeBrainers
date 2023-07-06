from django.db import models


class Author(models.Model):
    """
    Author model

    Attributes:
        first_name (CharField)
        last_name (CharField)
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
