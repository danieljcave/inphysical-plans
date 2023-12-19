from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from django.http import HttpResponse


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-date_created")
    template_name = "index.html"
    paginate_by = 6
