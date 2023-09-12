from django.test import TestCase

from ..models import Author, Book


class BookModelTest(TestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(
            first_name='test_name',
            last_name='test_last_name'
        )

        self.book = Book.objects.create(
            title='test_title',
            author_id=self.author
        )

    def test_book_creation(self):
        pass
