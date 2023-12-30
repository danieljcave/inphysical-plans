from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment


class TestViews(TestCase):
    """
    Test Blog App Views
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

    def test_blog_post_list(self):
        """Test blog post list retrieval and correct template used"""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_get_blog_post_page(self):
        """Test blog_post retrieval and correct template used"""
        response = self.client.get(
            reverse('blog_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_post.html', 'base.html')

    def test_get_post_add(self):
        """Test add_post retrieval and correct template used"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/post/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post.html', 'base.html')

    def test_get_post_delete(self):
        """Test delete_post retrieval and correct template used"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse('delete_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_post.html', 'base.html')

    def test_get_post_update(self):
        """Test update_post retrieval and correct template used"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse('update_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_post.html', 'base.html')

    def test_get_post_add(self):
        """Test add_post retrieval and correct template used"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/post/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post.html', 'base.html')

    def test_post_comment(self):
        """Test post commenting feature"""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('blog_post', args=[self.post.slug]),
            data={'body': 'testcomment'})
        self.assertRedirects(
            response, reverse('blog_post', args=[self.post.slug]))

    def test_post_like(self):
        """Test feature to like a blog post"""
        self.client.login(username='testuser', password='testpass')
        likes = self.post.likes.count()
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]))
        self.assertRedirects(response, reverse(
            'blog_post', args=[self.post.slug]))
        self.assertEqual(self.post.likes.count(), likes+1)
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]))
        self.assertRedirects(response, reverse(
            'blog_post', args=[self.post.slug]))
        self.assertEqual(self.post.likes.count(), likes)

    def test_404_page(self):
        """Test if users 404 error code uses custom error 404 page"""
        response = self.client.get('non_existent_url')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
