from rest_framework import generics
from rest_framework import viewsets

from ..models import Book
from ..serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    Book view that lists all books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    Book viewset
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
