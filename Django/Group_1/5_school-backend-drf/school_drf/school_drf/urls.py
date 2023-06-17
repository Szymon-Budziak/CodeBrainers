from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('rest_api.routing', 'rest_api'), namespace="api")),
    path('api-auth-token/', obtain_auth_token),
]
