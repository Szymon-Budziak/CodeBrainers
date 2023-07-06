from django.db import models
from django.contrib.auth.models import User

from . import Book


class Borrow(models.Model):
    """
    Borrow model

    Attributes:
        user_id (ForeignKey)
        book_id (ForeignKey)
        borrow_date (DateTimeField)
        return_date (DateTimeField)
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user_id.first_name} {self.user_id.last_name} {self.return_date.strftime('%Y-%m-%d %H:%M:%S')}"
