from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.template.defaultfilters import slugify


class Post(models.Model):
    """
    Database model for blog posts
    """
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
        """Set's the order of blog posts in acending order"""
        ordering = ['-date_created']

    def __str__(self):
        """Returns the blog sting as a title"""
        return self.title

    def total_likes(self):
        """Returns the amount of blog post likes"""
        return self.likes.count()

    def get_absolute_url(self):
        """Returns a succesfull blog post to a related slug url"""
        return reverse('blog_post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """Override save method using slugify"""
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Database model for comments
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_comment")
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        """Set's the order of comments in acending order"""
        ordering = ['date_created']

    def __str__(self):
        """Returns a comment with body and name"""
        return f"Commented {self.body} by {self.author}"
