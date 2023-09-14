from django.test import TestCase

from ..models import Author, Book
from ..serializers import BookSerializer


class BookSerializerTest(TestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(
            first_name='test_name',
            last_name='test_last_name'
        )

        self.book = Book.objects.create(
            title='test_title',
            author_id=self.author
        )

        self.serializer_data = {
            'title': 'test_title',
            'author_id': self.author.id
        }

    def test_serializer_contains_expected_fields(self):
        serializer = BookSerializer(instance=self.book)
        data = serializer.data

        self.assertEqual(set(data.keys()), {'id', 'title', 'author_id'})
        self.assertEqual(data['title'], self.book.title)
        self.assertEqual(data['author_id'], self.book.author_id.id)

    def test_serializer_create_valid_date(self):
        serializer = BookSerializer(instance=self.book, data=self.serializer_data)

        self.assertTrue(serializer.is_valid())
        new_book = serializer.save()
        self.assertEqual(new_book.author_id.id, self.serializer_data['author_id'])
        self.assertEqual(new_book.title, self.serializer_data['title'])

    def test_serializer_create_invalid_data(self):
        invalid_data = {
            'title': 'test_title',
            'author_id': None
        }

        serializer = BookSerializer(instance=self.book, data=invalid_data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_update_valid_data(self):
        updated_data = {
            'title': 'updated_title',
            'author_id': self.author
        }

        serializer = BookSerializer(instance=self.book, data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()

        serializer.update(instance=self.book, validated_data=updated_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.data['title'], updated_data['title'])
        self.assertEqual(serializer.data['author_id'], updated_data['author_id'].id)

    def test_serializer_update_invalid_data(self):
        invalid_data = {
            'title': 'test_title',
            'author_id': None
        }

        serializer = BookSerializer(instance=self.book, data=invalid_data, partial=True)
        self.assertFalse(serializer.is_valid())
