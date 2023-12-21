from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    excerpt = models.TextField(blank=True, max_length=200)
    image_upload = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"Commented {self.body} by {self.name}"
