from django.shortcuts import render
from django.views import generic, View
from .models import Profile


def ProfileView(request):
    return render(request, "profile.html")
