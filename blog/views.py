from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class PostList(generic.ListView):
    """Display list for blog preview paginated by 6"""
    model = Post
    queryset = Post.objects.all().order_by("-date_created")
    template_name = "index.html"
    paginate_by = 6


class BlogPost(View):
    """
    View for displaying a blog post on a single page,
    which includes the ability to comment and like a post.
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Get a method for retrieving blog post details which include,
        comments, like and to rende the blog post page.
        """
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('-date_created')
        liked = False
        if post.likes.exists():
            liked = True

        return render(
            request,
            "blog_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        A post method to validate comment submissions, to save and re-load
        the blog post page.
        Add a successful comment post message for user feedback
        """
        if request.user.is_authenticated:
            queryset = Post.objects.all()
            post = get_object_or_404(queryset, slug=slug)
            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                messages.success(request, 'Comment Added')

        return HttpResponseRedirect(reverse('blog_post', args=[slug]))


class CreatePost(LoginRequiredMixin,
                 SuccessMessageMixin,
                 generic.CreateView):
    """
    View to allow users to create a new blog post
    Add a successfully created post message for user feedback
    """
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    success_message = 'Added Post'

    def form_valid(self, form):
        """
        Validate the form after connecting the
        form author to the current user
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin,
                 SuccessMessageMixin,
                 UserPassesTestMixin,
                 generic.UpdateView):
    """
    View to allows users to update their blog post
    on the blog post page
    Add a successful updated post message for user feedback
    """
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm
    success_message = 'Updated Post'

    def form_valid(self, form):
        """
        Validate the form after connecting the
        form author to the current user
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Using UserPassesTestMixin to test if the user that
        is logged in and is the blog post author
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UpdateComment(LoginRequiredMixin,
                    SuccessMessageMixin,
                    UserPassesTestMixin,
                    generic.UpdateView):
    """
    View to allow users to update their comment
    on the blog post page
    Add a successfully updated comment message for user feedback
    """
    model = Comment
    template_name = 'update_comment.html'
    form_class = CommentForm
    success_message = 'Updated Comment'

    def get_success_url(self):
        """Success url for post associated with the comment"""
        slug = self.kwargs['slug']
        return reverse_lazy('blog_post', kwargs={'slug': slug})

    def form_valid(self, form):
        """
        Validate the form after connecting the form
        author to current logged-in user
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Using UserPassesTestMixin to test if the user that
        is logged in is the blog post author
        """
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class DeleteComment(LoginRequiredMixin,
                    SuccessMessageMixin,
                    UserPassesTestMixin,
                    generic.DeleteView):
    """
    View to allow users to delete their comments on
    the blog post page
    Add a successful deleted comment message for user feedback
    """
    model = Comment
    template_name = 'blog_post.html'
    success_message = 'Deleted Comment'

    def get_success_url(self):
        """Success url for post associated with comment"""
        slug = self.kwargs['slug']
        return reverse_lazy('blog_post', kwargs={'slug': slug})

    def delete(self, request, *args, **kwargs):
        """Create a success message on the delete view"""
        messages.success(self.request, self.success_message)
        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def test_func(self):
        """
        Using UserPassesTestMixin to test if the user that
        is logged in is the blog post author
        """
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class DeletePost(LoginRequiredMixin,
                SuccessMessageMixin,
                 UserPassesTestMixin,
                 generic.DeleteView):
    """
    View to allow users to delete their blog posts
    on the blog post page
    Add a successful deleted post message for user feedback
    """
    model = Post
    template_name = 'blog_post.html'
    success_message = 'Deleted Post'

    def get_success_url(self):
        """Success url for post deleted"""
        return reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        """Create a success message on the delete view"""
        return super(DeletePost, self).delete(request, *args, **kwargs)

    def test_func(self):
        """
        Using UserPassesTestMixin to test if the user that
        is logged in is the blog post author
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class LikePost(LoginRequiredMixin, View):
    """
    View to add or remove likes on the blog post page.
    """

    def post(self, request, slug, *args, **kwargs):
        """
        Post method to toggle blog post likes and
        redirects to the blog post page.
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_post', args=[slug]))


def handler403(request, exception):
    """
    Display custom 403 page
    """
    return render(request, "403.html", status=403)


def handler404(request, exception):
    """
    Display custom 404 page
    """
    return render(request, "404.html", status=404)


def handler405(request, exception):
    """
    Display custom 405 page
    """
    return render(request, "405.html", status=405)


def handler500(request):
    """
    Display custom 500 page
    """
    return render(request, "500.html", status=500)
