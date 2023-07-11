from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ..models import Book
from ..serializers import BookSerializer
from ..permissions import ReadOnly


class BookViewList(ListCreateAPIView):
    """
    Book view list
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [(IsAuthenticated & ReadOnly) | IsAdminUser]
