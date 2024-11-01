from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_successful(self):
        """Test creating a user is successful."""
        email = "valen@example.com"
        password = "testpass123"
        name = "Valentina"
        last_name = "Perez"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name=name,
            last_name=last_name,
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.name, name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.com", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password="sample123",
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="admin123",
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
