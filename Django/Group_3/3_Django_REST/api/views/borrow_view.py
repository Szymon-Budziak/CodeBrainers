from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError

from ..models import Borrow
from ..serializers import BorrowSerializer


class BorrowListView(generics.ListCreateAPIView):
    """
    Borrow view that lists all borrows
    """
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class BorrowRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    """
    Borrow view that retrieves and deletes single borrow
    """
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def delete(self, request, *args, **kwargs):
        borrow = Borrow.objects.filter(pk=kwargs['pk'], user_id=self.request.user)
        if borrow.exists():
            return super().delete(request, *args, **kwargs)
        raise ValidationError('You are not the owner.')


class BorrowUpdateView(generics.UpdateAPIView):
    """
    Borrow view that updated single borrow
    """
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = (IsAuthenticated,)
