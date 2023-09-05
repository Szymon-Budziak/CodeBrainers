from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from django.utils import timezone

from ..models import Borrow
from ..serializers import BorrowSerializer, BorrowReturnBookSerializer


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
            return super().destroy(request, *args, **kwargs)
        raise ValidationError('You are not the owner.')


class BorrowUpdateView(generics.UpdateAPIView):
    """
    Borrow view that updated single borrow
    """
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        borrow = Borrow.objects.filter(pk=kwargs['pk'], user_id=self.request.user)
        if borrow.exists():
            return super().update(request, *args, **kwargs)
        raise ValidationError('You are not the owner.')


class BorrowReturnBookUpdateView(generics.UpdateAPIView):
    """
    Borrow return book view that updates return_date field in Borrow
    """
    queryset = Borrow.objects.all()
    serializer_class = BorrowReturnBookSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        borrow = Borrow.objects.filter(pk=kwargs['pk'], user_id=self.request.user)
        if borrow.exists():
            return super().update(request, *args, **kwargs)
        raise ValidationError('You are not the owner.')

    def perform_update(self, serializer):
        current_timezone = timezone.get_current_timezone()
        # 1st method
        # serializer.save(return_date=timezone.now().astimezone(current_timezone))
        # 2nd method
        serializer.instance.return_date = timezone.now().astimezone(current_timezone)
        serializer.save()
