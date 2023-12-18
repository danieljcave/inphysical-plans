from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'date_created')
    search_fields = ['title', 'content']
