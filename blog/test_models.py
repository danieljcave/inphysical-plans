from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post, Comment


class TestModels(TestCase):
    """
    Test Blog and Comment Model
    """
    @classmethod
    def setUp(self):
        """Create user, post and comment data"""
        self.user = User.objects.create(username='testuser')
        self.user.set_password('testpass')
        self.user.save()

        self.post = Post.objects.create(
            title='test post',
            slug='test-post',
            author=self.user,
        )

        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='test comment'
        )

    def test_str_for_post_model(self):
        """Test the __str__ method for post"""
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_str_comment_model(self):
        """Test the __str__ method for comment"""
        self.assertEqual(
            self.comment.__str__(),
            f'Commented {self.comment.body} by {self.comment.author}'
        )

    def test_absolute_url_post(self):
        """Test absolute_url for post"""
        self.assertEqual(self.post.get_absolute_url(), f'/{self.post.slug}/')
