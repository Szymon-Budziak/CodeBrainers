from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from ..models import Author, Book
from ..serializers import BookSerializer


class BookViewTest(TestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(
            first_name='test_name',
            last_name='test_last_name'
        )

        self.book1 = Book.objects.create(
            title='test_title_1',
            author_id=self.author
        )

        self.book2 = Book.objects.create(
            title='test_title_2',
            author_id=self.author
        )

        self.client = APIClient()

    def test_list_books(self):
        response = self.client.get(reverse('book_list'))

        self.assertEqual(response.status_code, 200)

        expected_data = BookSerializer([self.book1, self.book2], many=True).data

        self.assertEqual(response.data, expected_data)

    def test_list_books_empty(self):
        Book.objects.all().delete()

        response = self.client.get(reverse('book_list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])
