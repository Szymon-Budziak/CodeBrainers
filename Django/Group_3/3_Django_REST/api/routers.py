from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'authors', AuthorViewSet, basename='author_list')
router.register(r'books', BookViewSet, basename='book_list')

urlpatterns = router.urls
