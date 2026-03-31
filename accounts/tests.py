from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class SignUpViewTest(APITestCase):
    def setUp(self):
        self.signup_url = reverse("account_signup")  # Ensure this matches your urls.py name
        self.user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "john@example.com",
            "password1": "securepassword123",
            "password2": "securepassword123",
        }

    def test_signup_successful(self):
        """Test that a user can sign up with valid data."""
        response = self.client.post(self.signup_url, self.user_data, format="json")

        # Check response status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if user actually exists in the DB
        user = User.objects.get(username=self.user_data["username"])
        self.assertEqual(user.email, self.user_data["email"])

        # Verify password is NOT stored as plain text (hashed)
        self.assertNotEqual(user.password, self.user_data["password1"])
        self.assertTrue(user.check_password(self.user_data["password1"]))

    def test_signup_duplicate_username(self):
        """Test that signing up with an existing username returns an error."""
        # Create initial user
        User.objects.create_user(username="johndoe", password="somepassword")

        response = self.client.post(self.signup_url, self.user_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertEqual(response.data["error"], "User already exists")

    def test_signup_invalid_data(self):
        """Test signup fails if required fields are missing."""
        invalid_data = {"username": "short"}  # Missing password, etc.
        response = self.client.post(self.signup_url, invalid_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
