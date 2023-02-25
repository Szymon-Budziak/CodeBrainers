from django.urls import path
from .views import chat, chats

urlpatterns = [
    path("", chats, name="chats"),
    path("<slug:slug>/", chat, name="chat"),
]
