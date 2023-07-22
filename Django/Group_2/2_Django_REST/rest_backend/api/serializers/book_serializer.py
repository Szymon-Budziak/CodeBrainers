from rest_framework import serializers
from ..models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Book serializer
    """
    author_first_name = serializers.ReadOnlyField(source='author_id.first_name')
    author_last_name = serializers.ReadOnlyField(source='author_id.last_name')

    class Meta:
        model = Book
        fields = ('id', 'title', 'author_id', 'author_first_name', 'author_last_name')
