from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from ..serializers import TokenSerializer


class UserTokenList(ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Token.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        token = Token.objects.filter(user=self.request.user)
        if token.exists():
            return self.list(request, *args, **kwargs)
        else:
            token = Token.objects.create(user=self.request.user)
            return self.list(request, *args, **kwargs)
