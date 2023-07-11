from rest_framework.generics import ListAPIView

from ..models import Author
from ..serializers import AuthorSerializer


class AuthorViewList(ListAPIView):
    """
    Author view list
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
