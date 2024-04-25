"""
URL mappings for the user API.
"""
from django.urls import path, include
from users.api.views.user_view import user_view
from users.api.views.user_session_view import UserSessionView
from rest_framework.routers import DefaultRouter

from users.api import views

router = DefaultRouter()
router.register("users", UserSessionView, basename="session")


app_name = "users"

urlpatterns = [
    path('', include(router.urls)),
    path("me/", view=user_view, name="me"),
]


