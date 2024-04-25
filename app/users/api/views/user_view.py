from users.api.serializers.user_serializer import UserSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model


User = get_user_model()


class UserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


user_view = UserView.as_view()