from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from rest_framework.exceptions import PermissionDenied

from posts.forms import PostForm
from posts.models import Post


class PostView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.user, request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.save()
            return redirect('posts:posts')
    else:
        form = PostForm(request.user)
    return render(request, 'add_post.html', {'form': form})


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'text']

    def get_object(self, *args, **kwargs):
        obj = super(UpdatePostView, self).get_object(*args, **kwargs)
        if not obj.creator == self.request.user:
            raise PermissionDenied
        return obj


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts:posts')

    def get_object(self, *args, **kwargs):
        obj = super(DeletePostView, self).get_object(*args, **kwargs)
        if not obj.creator == self.request.user:
            raise PermissionDenied
        return obj
