import logging
from django.test import TestCase, Client
from django.urls import reverse
from user_app.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point
from django.conf import settings

# Initialize logger
logger = logging.getLogger(__name__)

User = get_user_model()

class ViewsTestCase(TestCase):
    def setUp(self):
        """
        Set up test data for the test cases.
        """
        logger.info("Setting up test data...")
        self.client = Client()
        self.password = "password123"
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password=self.password,
            first_name="Test",
            last_name="User",
            phone_number="1234567890",
            home_address="123 Test Street",
            location=Point(77.2090, 28.6139)  # New Delhi coordinates
        )
        self.edit_user_url = reverse('edit_user', args=[self.user.id])
        self.login_url = reverse('do_login')
        self.logout_url = reverse('logout')
        self.manage_users_url = reverse('manage_users')
        self.map_url = reverse('map')
        logger.info("Test data setup complete.")

    def test_do_login_success(self):
        """
        Test successful login with valid credentials.
        """
        logger.info("Testing successful login...")
        response = self.client.post(self.login_url, {
            'email': 'testuser@example.com',
            'password': self.password
        }, follow=True)
        logger.debug(f"Response status code: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')
        logger.info("Successful login test passed.")

    def test_do_login_failure(self):
        """
        Test login failure with invalid credentials.
        """
        logger.info("Testing login failure...")
        response = self.client.post(self.login_url, {
            'email': 'wrong@example.com',
            'password': 'wrongpassword'
        }, follow=True)
        logger.debug(f"Response status code: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        logger.info("Login failure test passed.")

    def test_do_logout(self):
        """
        Test logout functionality.
        """
        logger.info("Testing logout functionality...")
        self.client.login(username='testuser@example.com', password=self.password)
        response = self.client.get(self.logout_url, follow=True)
        logger.debug(f"Response status code: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        logger.info("Logout test passed.")

    def test_manage_users_authenticated(self):
        """
        Test manage_users view for authenticated users.
        """
        logger.info("Testing manage_users view for authenticated users...")
        login_successful = self.client.login(username='testuser', password=self.password)
        logger.debug(f"Login successful: {login_successful}")
        self.assertTrue(login_successful, "Login failed")

        response = self.client.get(self.manage_users_url)
        logger.debug(f"Response status code: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')
        logger.info("Authenticated manage_users test passed.")

    def test_manage_users_unauthenticated(self):
        """
        Test manage_users view for unauthenticated users.
        """
        logger.info("Testing manage_users view for unauthenticated users...")
        response = self.client.get(self.manage_users_url, follow=True)
        logger.debug(f"Response status code: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        logger.info("Unauthenticated manage_users test passed.")

    def test_edit_user_profile_success(self):
        """
        Test successful update of user profile.
        """
        logger.info("Testing successful update of user profile...")
        self.client.login(username='testuser@example.com', password=self.password)
        response = self.client.post(self.edit_user_url, {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'first_name': 'Updated',
            'last_name': 'User',
            'phone_number': '9876543210',
            'home_address': '456 Updated Street',
            'location': 'POINT(77.2090 28.6139)'
        })
        logger.debug(f"Response status code: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {'status': 'success', 'message': 'User profile updated successfully!'}
        )
        updated_user = CustomUser.objects.get(id=self.user.id)
        self.assertEqual(updated_user.username, 'updateduser')
        self.assertEqual(updated_user.email, 'updateduser@example.com')
        logger.info("Successful update of user profile test passed.")

    def test_edit_user_profile_failure(self):
        """
        Test failure to update user profile with invalid user ID.
        """
        logger.info("Testing failure to update user profile with invalid user ID...")
        self.client.login(username='testuser@example.com', password=self.password)
        invalid_url = reverse('edit_user', args=['999'])  # Non-existent user ID
        response = self.client.post(invalid_url, {
            'username': 'updateduser'
        })
        logger.debug(f"Response status code: {response.status_code}")
        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(
            response.content,
            {'status': 'error', 'message': 'User not found!'}
        )
        logger.info("Failure to update user profile test passed.")

    def test_map_view(self):
        """
        Test map view for authenticated users.
        """
        logger.info("Testing map view for authenticated users...")
        self.client.login(username='testuser', password=self.password)
        response = self.client.get(self.map_url)
        logger.debug(f"Response status code: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'map.html')
        self.assertIn('user_locations', response.context)
        self.assertEqual(response.context['api_key'], settings.GOOGLE_MAPS_API_KEY)  # Check if the API key from settings is passed
        logger.info("Map view test passed.")