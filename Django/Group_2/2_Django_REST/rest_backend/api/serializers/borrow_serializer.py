from rest_framework import serializers
from ..models import Borrow


class BorrowSerializer(serializers.ModelSerializer):
    """
    Borrow serializer
    """
    user_first_name = serializers.ReadOnlyField(source='user_id.first_name')
    user_last_name = serializers.ReadOnlyField(source='user_id.last_name')
    user_email = serializers.ReadOnlyField(source='user_id.email')
    user_id = serializers.ReadOnlyField(source='user_id.id')
    return_date = serializers.ReadOnlyField()

    class Meta:
        model = Borrow
        fields = ('id', 'user_id', 'user_first_name', 'user_last_name', 'user_email', 'book_id', 'borrow_date',
                  'return_date')


class BorrowReturnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ('id',)
