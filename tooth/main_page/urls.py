from django.conf.urls import *
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from . import views, models

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^about', views.AboutView.as_view(), name='about'),
	url(r'^login', views.login, name='login'),
	url(r'^account', views.office_account, name='office_account'),
	url(r'^dentists', views.DentistsListView.as_view(), name='dentists'),
	url(r'^dentist/(?P<slug>[a-zA-Z0-9-]+)/?', views.DentistDetailView.as_view(), name='dentist'),
	url(r'^offices', views.OfficesListView.as_view(), name='offices'),
	url(r'^office/(?P<slug>[a-zA-Z0-9-]+)/?', views.OfficeDetailView.as_view(), name='office'),
	url(r'^patients', login_required(views.PatientsListView.as_view()), name='patients'),
	url(r'^patient/(?P<slug>[a-zA-Z0-9-]+)/?', login_required(views.PatientDetailView.as_view()), name='patient' ),
	url(r'^contact', views.contact, name='contact'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'^search_dentist', views.search_dentist, name='search_dentist'),
    url(r'^search_patient', views.search_patient, name='search_patient'),
    url(r'^search_office', views.search_office, name='search_office'),
]
