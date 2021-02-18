# 'LoginRequiredMixin' avoiding form user to create post when he logged out
from abc import ABC

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

##########
def home(request):
    data = {'posts': Post.objects.all()}
    return render(request, 'app/home.html', data)


##########
class PostLIstView(ListView):
    model = Post
    template_name = 'app/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 2


##########
class UserPostLIstView(ListView):
    model = Post
    template_name = 'app/user_posts.html'
    context_object_name = 'posts'
    # ordering = ['-date']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


##########
class PostDetailView(DetailView):
    model = Post


##########
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


##########
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ABC):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


##########
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView, ABC):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

##########
def about(request):
    return render(request, 'app/about.html', {'title': 'About'})



