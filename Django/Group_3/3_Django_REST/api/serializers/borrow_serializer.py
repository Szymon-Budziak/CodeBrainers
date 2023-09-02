from rest_framework import serializers

from ..models import Borrow


class BorrowSerializer(serializers.ModelSerializer):
    """
    Borrow serializer
    """
    book = serializers.ReadOnlyField(source='book_id.title')
    author_first_name = serializers.ReadOnlyField(source='book_id.author_id.first_name')
    author_last_name = serializers.ReadOnlyField(source='book_id.author_id.last_name')
    user_first_name = serializers.ReadOnlyField(source='user_id.first_name')
    user_last_name = serializers.ReadOnlyField(source='user_id.last_name')
    user_email = serializers.ReadOnlyField(source='user_id.email')
    user_id = serializers.ReadOnlyField(source='user_id.id')

    class Meta:
        model = Borrow
        fields = ('id', 'user_id', 'user_first_name', 'user_last_name', 'user_email', 'book_id', 'book',
                  'author_first_name', 'author_last_name', 'borrow_date', 'return_date')
