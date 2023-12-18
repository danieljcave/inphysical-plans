from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'post': post
    }
    return render(request, 'index.html', context)


post = [
    {
        'author': 'Admin',
        'title': 'Blog Post 1',
        'content': 'This is the first blog post',
        'date_created': '18th Dec, 2023'
    },
    {
        'author': 'Admin2',
        'title': 'Blog Post 2',
        'content': 'This is the second blog post',
        'date_created': '19th Dec, 2023'
    },
    {
        'author': 'Admin3',
        'title': 'Blog Post 3',
        'content': 'This is the third blog post',
        'date_created': '19th Dec, 2023'
    },
    {
        'author': 'Admin4',
        'title': 'Blog Post 4',
        'content': 'This is the fourth blog post',
        'date_created': '19th Dec, 2023'
    }
]
