from .models import Profile
from django import forms


class ProfileForm(forms.ModelForm):
    """
    Profile Update Form
    """
    class Meta:
        model = Profile
        fields = [
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
        ]
