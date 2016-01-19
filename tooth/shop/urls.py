from django.conf.urls import *
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from . import views, models

urlpatterns = [
	url(r'^/category/(?P<slug>[a-zA-Z0-9-]+)/?$', views.CategoryView.as_view(), name="shop_category"),
    url(r'^/tag/(?P<slug>[a-zA-Z0-9-]+)/?$', views.TagView.as_view(), name="shop_tag"),
	url(r'^/product/(?P<slug>[a-zA-Z0-9-]+)/?$', views.ProductDetailView.as_view(), name='shop_detail'),
	url(r'^$', views.ShopIndexView.as_view(), name='shop_index'),
	]