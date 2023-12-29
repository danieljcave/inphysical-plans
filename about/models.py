from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class Profile(models.Model):
    """
    Database model for user profiles
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField(
        'image', default="https://res.cloudinary.com/dg7zlxltx/image/upload/v1703632848/pfp_default.png_l6pv4p.png")  # noqa
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField()
    occupation = models.CharField(max_length=50, blank=True)
    country = CountryField(blank=True)
    gym_focus = models.CharField(max_length=255, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Signal receiver to create a users profile when a user create a new account


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal reveiver to save a users profile when a new account is created


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
