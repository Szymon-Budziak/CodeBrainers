from rest_framework import serializers
from ..models import Borrow


class BorrowSerializer(serializers.ModelSerializer):
    """
    Borrow serializer
    """

    class Meta:
        model = Borrow
        fields = ['id', 'user_id', 'book_id', 'borrow_date', 'return_date']
