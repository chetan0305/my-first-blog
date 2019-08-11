from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # gives readable error page if object doesnt exist
    # post = Post.objects.get(pk=pk) # old way to write above, does not give good error page if object doesnt exist
    return render(request, 'blog/post_detail.html', {'post': post})
