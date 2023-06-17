from django.shortcuts import render
from .models import Author
from .serializers import AuthorSerializer
from rest_framework import generics


class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorInstanceView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


def index_view(request):
    return render(request, "bookreview/index.html", {"authors": Author.objects.all()})
