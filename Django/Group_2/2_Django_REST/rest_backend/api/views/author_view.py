from rest_framework.generics import ListCreateAPIView

from ..models import Author
from ..serializers import AuthorSerializer


class AuthorViewList(ListCreateAPIView):
    """
    Author view list
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
