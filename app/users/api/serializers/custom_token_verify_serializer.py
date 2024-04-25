from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from packages.token import check_token_validity


class CustomTokenVerifySerializer(serializers.Serializer):
    """Serializer for validate jwt token"""

    token = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get("token", None)

        if not check_token_validity(token):
            raise ValidationError({"detail": "Token is invalid or expired"})

        return token