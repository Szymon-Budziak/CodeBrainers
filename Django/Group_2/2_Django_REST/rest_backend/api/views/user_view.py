from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

from ..serializers import UserSerializer
from ..models import ActionAuthorization


class UserCreate(CreateAPIView):
    """
    User create view
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        subject = "Activate your account"
        token_auth = ActionAuthorization.objects.create(user=user, info="Account is not activated.")
        message = render_to_string('../templates/api/account_activation.html',
                                   {'user': user,
                                    'domain': '127.0.0.1.8000',
                                    'token': token_auth,
                                    'token_id': token_auth.id})
        sender = 'youremail@gmail.com'
        recipients = [serializer.data['email']]
        send_mail(subject, message, sender, recipients)
