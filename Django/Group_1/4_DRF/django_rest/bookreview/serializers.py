from .models import Author, Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    search_url = serializers.SerializerMethodField("get_search_url")

    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'author', 'search_url')

    def get_search_url(self, obj):
        return f"http://www.isbnsearch.org/isbn/{obj.isbn}"


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True, source="book_set")

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'books')
