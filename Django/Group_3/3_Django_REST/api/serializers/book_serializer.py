from rest_framework import serializers

from ..models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Book serializer
    """

    class Meta:
        model = Book
        fields = ('id', 'title', 'author_id')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        return instance
