from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Profile
from blog.models import Post
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class ShowProfilePageView(generic.DetailView, View):
    """
    View to show users profile
    """
    model = Profile
    template_name = "profile.html"

    def get_context_data(self, *args, **kwargs):
        """
        Function to get users profile id from pk
        """
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])

        context["page_user"] = page_user
        return context


class EditProfile(LoginRequiredMixin,
                  SuccessMessageMixin,
                  UserPassesTestMixin,
                  generic.UpdateView):
    """
    View to edit users profile and update information
    """
    model = Profile
    template_name = "edit_profile_page.html"
    form_class = ProfileForm
    success_message = "Updated Profile"

    def get_success_url(self):
        """
        Redirect to users profile after succesfully editing profile,
        using a reverse_lazy after get_success_url
        """
        return reverse_lazy("show_profile_page", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        """
        Validate the form after connecting the
        profile user to current user request
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Using UserPassesTestMixin to test if the user that
        is logged in, is the profile user
        """
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False


class DeleteProfile(LoginRequiredMixin,
                    SuccessMessageMixin,
                    UserPassesTestMixin,
                    generic.DeleteView):
    """
    View for users to delete their profile and account.
    """
    model = Profile
    template_name = "profile.html"
    success_message = "Account Deleted"

    def get_success_url(self):
        """
        Success url for account deleted
        """
        return reverse('home')

    def delete(self, request, *args, **kwargs):
        """
        To delete users account and redirect to home page
        """
        self.object = self.get_object()
        self.object.user.delete()
        return HttpResponseRedirect(reverse("home"))

    def test_func(self):
        """
        Test that the user making request is the profiles user
        """
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False
