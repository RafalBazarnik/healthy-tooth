from django.conf.urls import *
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import ListView, DetailView
from . import views, feed, models

urlpatterns = [
	url(r'^$', views.BlogIndex.as_view(), name="blog"),
	url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$',
		views.PostDetail.as_view(), name="post_detail"),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$', views.CategoryView.as_view(), name="category"),
	url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$', views.TagView.as_view(), name="tag"),
	url(r'^search', views.search, name='search_result_blog'),
	url(r'^sitemap\.xml$', sitemap,
		{'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
		name='django.contrib.sitemaps.views.sitemap'),
	url(r'^feed/$', feed.LatestPosts(), name="feed"),
	]