from rest_framework import generics

from ..models import Author
from ..serializers import AuthorSerializer


class AuthorListView(generics.ListAPIView):
    """
    Author view that lists all authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
