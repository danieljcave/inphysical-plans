from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Profile
from blog.models import Post
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class ShowProfilePageView(generic.DetailView, View):
    model = Profile
    template_name = 'profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


class EditProfile(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UserPassesTestMixin,
                  generic.UpdateView):
    model = Profile
    template_name = 'edit_profile_page.html'
    form_class = ProfileForm
    success_message = 'Updated Profile'

    def get_success_url(self):
        return reverse_lazy('show_profile_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False
