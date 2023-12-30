from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class TestViews(TestCase):
    """
    Test About app views
    """
    @classmethod
    def setUp(self):
        """Create user profile"""
        self.user = User.objects.create(username='testuser')
        self.user.set_password('testpass')
        self.user.save()

    def test_user_profile(self):
        """Test user profile retrieval and correct template used"""
        response = self.client.get(
            reverse('show_profile_page', kwargs={"pk": self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html', 'base.html')

    def test_update_user_profile(self):
        """Test update user profile retrieval and correct template used"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse('edit_profile_page', kwargs={"pk": self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'edit_profile_page.html', 'base.html')

    def test_get_post_delete(self):
        """Test delete user profile retrieval and correct template used"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse('delete_profile', kwargs={"pk": self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html', 'base.html')
