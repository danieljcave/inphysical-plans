from .models import Comment, Post
from django_summernote.widgets import SummernoteWidget
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
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
