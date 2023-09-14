from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from ..models import Author
from ..serializers import AuthorSerializer


class AuthorListView(generics.ListAPIView):
    """
    Author view that lists all authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    Author viewset
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
