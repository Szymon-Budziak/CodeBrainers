from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from ..models import ActionAuthorization
from ..serializers import ActionAuthorizationSerializer


class ActionAuthorizationRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = ActionAuthorization.objects.all()
    serializer_class = ActionAuthorizationSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return ActionAuthorization.objects.filter(key=self.kwargs['token'])

    def put(self, request, *args, **kwargs):
        try:
            token = ActionAuthorization.objects.get(key=kwargs['token'])
            user = User.objects.get(id=token.user_id)
            user.is_active = True
            user.save()
            return self.update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise ValidationError('Error')

    def perform_update(self, serializer):
        serializer.save(info="Account has been activated!")
