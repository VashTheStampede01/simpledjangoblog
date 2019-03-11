from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.bloglist.as_view(), name = 'blog_list'),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.blogdetail.as_view(), name = 'blog_detail'),
    url(r'^news/$', views.newslist.as_view(), name = 'news_list'),
    url(r'^news/(?P<pk>[0-9]+)/$', views.newsdetail.as_view(), name = 'news_detail'),
    url(r'^article/$', views.articlelist.as_view(), name = 'article_list'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.articledetail.as_view(), name = 'article_detail'),
]