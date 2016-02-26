from django.conf.urls import *
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from . import views, models

urlpatterns = [
	url(r'^/category/(?P<slug>[a-zA-Z0-9-]+)/?$', views.CategoryView.as_view(), name="shop_category"),
    url(r'^/tag/(?P<slug>[a-zA-Z0-9-]+)/?$', views.TagView.as_view(), name="shop_tag"),
	url(r'^/product/(?P<slug>[a-zA-Z0-9-]+)/?$', views.ProductDetailView.as_view(), name='shop_detail'),
	url(r'^/new_purchase/$', views.PurchaseFormView.as_view(), name='new_purchase'),
	url(r'^/purchase_list/$', views.PurchaseListView.as_view(), name='purchase_list'),
	url(r'^/purchase/(?P<pk>[0-9]+)/?', views.PurchaseDetailView.as_view(), name='purchase_details'),
	url(r'^/office/purchase_list/$', views.PurchaseOfficeListView.as_view(), name="office_purchase_list"),
	url(r'^/office/purchase/update/(?P<pk>[0-9]+)/?', views.PurchaseStatusUpdate.as_view(), name='office_purchase_status_update'),
	url(r'^$', views.ShopIndexView.as_view(), name='shop_index'),
	]