from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-date_created")
    template_name = "index.html"
    paginate_by = 6


class BlogPost(View):

    def get(self, request, slug, *args, **kwargs):
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
        if request.user.is_authenticated:
            queryset = Post.objects.all()
            post = get_object_or_404(queryset, slug=slug)
            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()

        return HttpResponseRedirect(reverse('blog_post', args=[slug]))


class CreatePost(LoginRequiredMixin,
                 generic.CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin,
                 UserPassesTestMixin,
                 generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UpdateComment(LoginRequiredMixin,
                    UserPassesTestMixin,
                    generic.UpdateView):
    model = Comment
    template_name = 'update_comment.html'
    form_class = CommentForm

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('blog_post', kwargs={'slug': slug})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class DeleteComment(LoginRequiredMixin,
                    UserPassesTestMixin,
                    generic.DeleteView):
    model = Comment
    template_name = 'blog_post.html'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('blog_post', kwargs={'slug': slug})

    def delete(self, request, *args, **kwargs):
        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class DeletePost(LoginRequiredMixin,
                 UserPassesTestMixin,
                 generic.DeleteView):
    model = Post
    template_name = 'blog_post.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        return super(DeletePost, self).delete(request, *args, **kwargs)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class LikePost(LoginRequiredMixin, View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_post', args=[slug]))
