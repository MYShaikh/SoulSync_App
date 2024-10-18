from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from ProjectModels.models import CustomUser

class LoginPageTest(TestCase):

    def setUp(self):
        # Create a test user
        self.email = 'aa@gmail.com'
        self.password = '123'
        self.user = CustomUser.objects.create_user(email=self.email, password=self.password)

    def test_login(self):
        # Use Django's reverse function to get the login URL
        login_url = reverse('login')  # Ensure your login URL is named 'login'

        # Make a POST request to the login page with the test user's credentials
        response = self.client.post(login_url, {
            'email': self.email,
            'password': self.password
        })

        # Check if the login was successful (response should redirect after login)
        self.assertEqual(response.status_code, 302)  # 302 is for a successful redirect
        self.assertRedirects(response, reverse('userinfo'))  # Assuming you redirect to 'home' after login

        # Check if the user is now logged in
        # self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_invalid_login(self):
        # Use the login URL
        login_url = reverse('login')

        # Make a POST request with incorrect credentials
        response = self.client.post(login_url, {
            'email': self.email,
            'password': 'wrongpassword'
        })

        # Check if the login fails (usually a 200 status with the login page displayed again)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password")  # Customize for your template message

        # Check if the user is not logged in
        # self.assertFalse(response.wsgi_request.user.is_authenticated)
