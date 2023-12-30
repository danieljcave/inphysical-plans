from .models import Comment, Post
from django_summernote.widgets import SummernoteWidget
from django import forms


class CommentForm(forms.ModelForm):
    """
    Comments submition form.
    """
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    Comments form for posting comments.
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'image_upload',
            'content',
        ]
        widgets = {
            'content': SummernoteWidget(),
        }
