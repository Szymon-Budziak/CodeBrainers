from django.urls import path
from .views import *

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('borrows/', BorrowListView.as_view(), name='borrow_list'),
    path('borrows/<int:pk>/', BorrowRetrieveDestroyView.as_view(), name='borrow_retrieve_destroy'),
    path('borrows/<int:pk>/edit/', BorrowUpdateView.as_view(), name='borrow_update')
]
