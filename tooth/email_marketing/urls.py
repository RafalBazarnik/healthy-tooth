from django.conf.urls import *
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from . import views

urlpatterns = [
	url(r'^/emails_list/$', views.MarketingEmailList.as_view(), name='emails_list'),
	url(r'^/emails_detail/(?P<pk>[0-9]+)/?', views.MarketingEmailDetail.as_view(), name='email_detail'),
	url(r'^$', views.NewMarketingEmail.as_view(), name='new_marketing_email'),
	]