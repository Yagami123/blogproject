from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from markdown import markdown

from blog.models import Post, Category


def index(request):
    # return HttpResponse("欢迎光临我的博客!")
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def blog(request):
    return render(request, 'blog/blog.html')


def about(request):
    return render(request, 'blog/about.html')


def portfolio(request):
    return render(request, 'blog/portfolio.html')


def contact(request):
    return render(request, 'blog/contact.html')


def detail(request, pk):
    # 当pk对应的Post数据在数据库存在时，返回post；否则返回404错误
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown(post.body,
                         extensions=[
                             'markdown.extensions.extra',
                             'markdown.extensions.codehilite',
                             'markdown.extensions.toc',
                         ])
    return render(request, 'blog/detail.html', context={'post': post})


def archives(request, year, month):
    """文章按月排行归档"""
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
