from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from . import Book


class Borrow(models.Model):
    """
    Borrow model

    Attributes:
        user_id (ForeignKey): foreign key to User django model
        book_id (ForeignKey): foreign ket to Book model
        borrow_date (DateTimeField): date when book is borrowed
        return_date (DateTimeField): date when book is returned
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        current_timezone = timezone.get_current_timezone()
        formatted_date = self.borrow_date.astimezone(current_timezone).strftime("%d/%m/%Y %H:%M:%S")
        return f'{self.user_id.first_name} {self.user_id.last_name} - {formatted_date}'
