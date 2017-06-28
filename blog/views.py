from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def post_list(request):
    queryset_list = Post.objects.all().order_by("-date")
    paginator = Paginator(queryset_list, 1)

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    return render(request, 'blog/blog.html', {'object_list': queryset,})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post.html', {'post': post, 'quote': quote})