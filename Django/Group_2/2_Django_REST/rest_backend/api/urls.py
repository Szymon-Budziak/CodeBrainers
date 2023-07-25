from django.urls import path

from .views import *

urlpatterns = [
    path("authors/", AuthorViewList.as_view()),
    path("books/", BookViewList.as_view(), name="books_list"),
    path("borrows/", BorrowViewList.as_view(), name="borrows_list"),
    path("borrows/<int:pk>/", BorrowRetrieveDestroy.as_view(), name="borrows_retrieve_destroy"),
    path("borrows/<int:pk>/edit/", BorrowRetrieveUpdate.as_view(), name="borrows_retrieve_update"),
    path("borrows/<int:pk>/return/", BorrowReturnBookUpdate.as_view(), name="borrows_return_book_update"),
    path("user/create/", UserCreate.as_view(), name="user_create"),
    path("user/login/", UserTokenList.as_view(), name="token_login")
]
