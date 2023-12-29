from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    """
    Database model for user profiles in admin panel
    """
    search_field = ('user')
