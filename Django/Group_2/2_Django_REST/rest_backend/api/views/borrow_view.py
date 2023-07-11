from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ..models import Borrow
from ..serializers import BorrowSerializer
from ..permissions import ReadOnly


class BorrowViewList(ListCreateAPIView):
    """
    Borrow view list
    """
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [(IsAuthenticated & ReadOnly) | IsAdminUser]
