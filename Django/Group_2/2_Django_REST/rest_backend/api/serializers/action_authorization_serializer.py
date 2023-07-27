from rest_framework import serializers

from ..models import ActionAuthorization


class ActionAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionAuthorization
        fields = ('id', 'key', 'user', 'created', 'info')
        read_only_fields = ('key', 'user', 'created')
