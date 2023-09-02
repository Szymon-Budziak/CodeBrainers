from rest_framework import serializers

from ..models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Book serializer
    """

    class Meta:
        model = Book
        fields = ('id', 'title', 'author_id')
