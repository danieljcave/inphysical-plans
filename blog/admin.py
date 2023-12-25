from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Database model for blog posts in admin panel
    """
    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'date_created')
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Database model for comments in admin panel
    """
    list_display = ('body', 'post', 'date_created',)
    search_fields = ('email', 'body')
