from django.conf.urls import *
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from . import views, models

urlpatterns = [
	# login to admin panel
	# login to office panel
	# admin panel
	# office panel
	url(r'^dentists', views.DentistsListView.as_view(), name='dentists'),
	#url(r'^/dentist/(?P<slug>[a-zA-Z0-9-]+)/?$', ),
	# add new dentist form
	url(r'^offices/', views.OfficesListView.as_view(), name='offices'),
	# url(r'^/office/(?P<slug>[a-zA-Z0-9-]+)/?$', ),
	# add new office form
	# edit office data form
	url(r'^patients/', views.PatientsListView.as_view(), name='patients'),
	# url(r'^/patient/(?P<slug>[a-zA-Z0-9-]+)/?$', ),
	# add new patient form
	# edit patient form
	url(r'^contact/$', views.contact, name='contact'),
    url(r'^sent/$', views.message_sent, name='message_sent'),
    url(r'^', views.IndexView.as_view(), name='index'),
]
