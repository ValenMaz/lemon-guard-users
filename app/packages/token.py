from datetime import timedelta

import environ
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

env = environ.Env()


def check_token_validity(token):
    if not token:
        return False
    return isinstance(token, (AccessToken, str))


def get_access_token(token):
    try:
        token = AccessToken(token)
        token["user_type"] = token["user_type"]
        return token
    except Exception as error:
        print(f"Could not generate token with the given string {token = }. {error =}")
        return


def get_access_token_for_user(user):
    try:
        token = AccessToken.for_user(user)
        token["user_type"] = user.user_type
        return token
    except Exception as error:
        print(f"Could not generate access token for user {user = }. {error = }")
        return

def get_refresh_token_for_user(user):
    try:
        refresh_token = RefreshToken.for_user(user)
        refresh_token['user_type'] = user.user_type
        return refresh_token
    except Exception as error:
        print(f"Could not generate refresh token for user {user = }. {error = }")
        return


def get_user_from_token(user, token):
    try:
        access_token = get_access_token(token)
        return JWTAuthentication.get_user(user, access_token)
    except Exception as error:
        print(f"Could not extract user from {token = }. {error = }")