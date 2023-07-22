from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from django.utils import timezone

from ..models import Borrow
from ..serializers import BorrowSerializer, BorrowReturnBookSerializer


class BorrowViewList(ListCreateAPIView):
    """
    Borrow view list
    """
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class BorrowRetrieveDestroy(RetrieveDestroyAPIView):
    """
    Borrow view retrieve and destroy
    """
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        borrow = Borrow.objects.filter(user_id=self.request.user, pk=kwargs["pk"])
        if len(borrow) != 0:
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('You are not the owner.')


class BorrowRetrieveUpdate(RetrieveUpdateAPIView):
    """
    Borrow view retrieve and update
    """
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        borrow = Borrow.objects.filter(user_id=self.request.user, pk=kwargs["pk"])
        if borrow.exists():
            return super().put(request, *args, **kwargs)
        else:
            raise ValidationError('You are not the owner.')


class BorrowReturnBookUpdate(UpdateAPIView):
    """
    Borrow view update
    """
    queryset = Borrow.objects.all()
    serializer_class = BorrowReturnBookSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        borrow = Borrow.objects.filter(pk=kwargs["pk"], user_id=self.request.user)
        if borrow.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('You are not the owner.')

    def perform_update(self, serializer):
        local_timezone = timezone.get_default_timezone()
        serializer.instance.return_date = timezone.now().astimezone(local_timezone) + timezone.timedelta(2)
        serializer.save()
