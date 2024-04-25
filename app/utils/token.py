import os
from datetime import timedelta

import jwt
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.exceptions import AuthenticationFailed

from packages.token import get_access_token_for_user


def decode_token(token):
    allowed_algorithms = ["HS256"]
    key = settings.SECRET_KEY
    try:
        return jwt.decode(token, algorithms=allowed_algorithms, key=key)
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed(_("Verification link has expired"))
    except jwt.PyJWTError:
        raise AuthenticationFailed(_("Invalid token."))


def get_verification_token(user):
    token_lifetime = timedelta(days=int(os.environ.get("EMAIL_ACCESS_TOKEN_LIFETIME_DAYS")))
    try:
        access_token = get_access_token_for_user(user)

        if access_token:
            access_token.set_exp(lifetime=token_lifetime)

            return access_token
    except Exception as e:
        print("Could not get the access token:: ", e)
        return None