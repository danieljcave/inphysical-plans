from .models import Profile
from django_summernote.widgets import SummernoteWidget
from django_countries.widgets import CountrySelectWidget
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'user',
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
        widgets = {
            'bio': SummernoteWidget(),
            'country': CountrySelectWidget(),
        }
