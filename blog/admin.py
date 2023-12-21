from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'date_created')
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'date_created',)
    search_fields = ('name', 'email', 'body')
