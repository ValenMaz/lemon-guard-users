from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from packages.token import get_refresh_token_for_user
from django.db import models




class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user




class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="no surname",
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def tokens(self):
        refresh = get_refresh_token_for_user(self)

        return {"refresh": str(refresh), "access": str(refresh.access_token)}
