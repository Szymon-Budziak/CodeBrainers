from django.urls import path
from django.contrib.auth import views as django_views
from . import views

urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('signup/', views.signup, name="signup"),
    path('login/', django_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout/', django_views.LogoutView.as_view(), name="logout"),
]
