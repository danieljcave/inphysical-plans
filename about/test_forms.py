from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import ProfileForm


class TestProfileForm(TestCase):
    """
    Test Profile Form
    """

    def test_fields_are_explicit_in_profile_metaclass(self):
        """Test body field is explicit in comment metaclass"""
        form = ProfileForm()
        self.assertEqual(form.Meta.fields, [
            'profile_image',
            'first_name',
            'last_name',
            'bio',
            'occupation',
            'gym_focus',
            'country',
            'twitter_url',
            'facebook_url',
            'instagram_url',
            'website_url',
        ])
