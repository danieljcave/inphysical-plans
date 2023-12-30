from django.test import TestCase
from .forms import CommentForm, PostForm


class TestCommentForm(TestCase):
    """
    Test comment fields in comment form
    """

    def test_comment_body_is_required(self):
        """Test if the comment body is required"""
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_comment_metaclass(self):
        """Test body field is explicit in comment metaclass"""
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))

    def test_form_is_valid(self):
        """Test if comment form body is invalid"""
        form = CommentForm({'body': 'Test Comment'})
        self.assertTrue(form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        """Test if comment form body is valid"""
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid(), msg="Form is valid")


class TestPostForm(TestCase):
    """
    Test the fields in the post form
    """

    def test_blog_post_title_is_required(self):
        """Tests that the blog post title is required"""
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_blog_post_content_is_required(self):
        """Tests that the blog post content is required"""
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_comment_metaclass(self):
        """Test body field is explicit in post metaclass"""
        form = PostForm()
        self.assertEqual(form.Meta.fields, [
                         'title', 'image_upload', 'content',])
