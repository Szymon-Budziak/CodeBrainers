from django.urls import path
from .views import AuthorView, AuthorInstanceView

urlpatterns = [
    path('authors/', AuthorView.as_view(), name="authors-list"),
    path('authors/<int:pk>/', AuthorInstanceView.as_view(), name="authors-instance")
]
