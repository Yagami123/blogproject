from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # return HttpResponse("欢迎光临我的博客!")
    return render(
        request, 'blog/blog.html'
    )
