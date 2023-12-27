from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Profile
from blog.models import Post


class ShowProfilePageView(generic.DetailView, View):
    model = Profile
    template_name = 'profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context
