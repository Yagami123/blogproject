from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # return HttpResponse("欢迎光临我的博客!")
    return render(
        request, 'blog/index.html'
    )


def blog(request):
    return render(request, 'blog/blog.html')


def about(request):
    return render(request, 'blog/about.html')


def portfolio(request):
    return render(request, 'blog/portfolio.html')


def contact(request):
    return render(request, 'blog/contact.html')
