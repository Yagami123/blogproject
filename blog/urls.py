from django.conf.urls import url
from django.views.generic import RedirectView

from blog import views

# html href-->blog : href="{% url 'blog:archives' date.year date.month %}"
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^about/$', views.about, name='about'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^contact/$', views.contact, name='contact'),
    # url重定向
    url(r'index.html/$', RedirectView.as_view(pattern_name="index")),
    url(r'blog.html/$', RedirectView.as_view(pattern_name="blog")),
    url(r'about.html/$', RedirectView.as_view(pattern_name="about")),
    url(r'portfolio.html/$', RedirectView.as_view(pattern_name="portfolio")),
    url(r'contact.html/$', RedirectView.as_view(pattern_name="contact")),
    # url文章id
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    # 归档
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]

