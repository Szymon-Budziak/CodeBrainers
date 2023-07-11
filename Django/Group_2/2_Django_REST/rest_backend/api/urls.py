from django.urls import path

from .views import AuthorViewList, BookViewList, BorrowViewList

urlpatterns = [
    path("authors/", AuthorViewList.as_view()),
    path("books/", BookViewList.as_view(), name="books_list"),
    path("borrows/", BorrowViewList.as_view(), name="borrows_list")
]
