from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    image_upload = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"Commented {self.body} by {self.name}"
