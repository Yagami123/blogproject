from django.conf.urls import url
from django.views.generic import RedirectView

from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html/$', RedirectView.as_view(pattern_name="index")),  # url重定向
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^about/$', views.about, name='about'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^contact/$', views.contact, name='contact'),
]
