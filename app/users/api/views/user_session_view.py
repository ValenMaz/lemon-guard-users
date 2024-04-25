from django.contrib.auth import authenticate, logout
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.api.serializers.user_signup_serializer import SignUpSerializer
from users.api.serializers.user_login_serializer import LoginUserSerializer


class UserSessionView(viewsets.GenericViewSet):
    """Views to configure endpoints for sign up, log in and logout for users"""

    permission_classes_by_action = {
        "signup": [AllowAny],
        "login": [AllowAny],
        "logout": [AllowAny],
    }

    @action(detail=False, methods=["post"], url_path="signup")
    def signup(selfe, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "User created successfully"}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"], url_path="login")
    def login(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, **serializer.validated_data)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=["post"], url_path="logout")
    def logout(self, request):
        # Para JWT, el logout puede ser manejado por el cliente eliminando el token
        # Este método podría ser utilizado para acciones adicionales de cierre de sesión si es necesario
        return Response({"status": "Logout successful"}, status=status.HTTP_200_OK)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'signup':
            return SignUpSerializer
        elif self.action == 'login':
            return LoginUserSerializer
        return super().get_serializer_class()
