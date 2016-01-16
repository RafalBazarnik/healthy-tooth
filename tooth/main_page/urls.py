from django.conf.urls import *
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from . import views, models

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^about', views.AboutView.as_view(), name='about'),
	url(r'^login', views.login_user, name='login_user'),
	url(r'^logout', views.logout_user, name='logout_user'),
	url(r'^account', login_required(views.OfficeIndexView.as_view()), name="office_account"),
	url(r'^contact', views.contact, name='contact'),
    url(r'^thanks', views.thanks, name='thanks'),
	
	# url(r'^account', views.office_account, name='office_account'),
	url(r'^dentists', views.DentistsListView.as_view(), name='dentists'),
	url(r'^dentist/update/(?P<slug>[a-zA-Z0-9-]+)/?', login_required(views.DentistUpdateView.as_view()), name="dentist_update"),
	url(r'^dentist/(?P<slug>[a-zA-Z0-9-]+)/?', views.DentistDetailView.as_view(), name='dentist'),
	url(r'^new_dentist', login_required(views.DentistCreateView.as_view()), name="new_dentist"),
	
	# office
	url(r'^offices/appointment/', views.NewAppointmentView.as_view(), name="office_appointment"),
	url(r'^offices/appointment_edit/(?P<pk>[0-9]+)/?', login_required(views.EditAppointmentView.as_view()), name="appointment_edit"),
	url(r'^offices', views.OfficesListView.as_view(), name='offices'),
	url(r'^office/update/(?P<slug>[a-zA-Z0-9-]+)/?', login_required(views.OfficeUpdateView.as_view()), name="office_update"),
	url(r'^office/(?P<slug>[a-zA-Z0-9-]+)/?', views.OfficeDetailView.as_view(), name='office'),
	# url(r'^office/(?P<province>[a-zA-Z0-9-]+)/(?P<city>[a-zA-Z0-9-]+)/(?P<slug>[a-zA-Z0-9-]+)/?', views.OfficeDetailView.as_view(), name='office'),
	# url(r'^office/(?P<province>[a-zA-Z0-9-]+)/(?P<city>[a-zA-Z0-9-]+)/?', , name='office_city'),

	# patients
	url(r'^patients', login_required(views.PatientsListView.as_view()), name='patients'),
	url(r'^patient/update/(?P<slug>[a-zA-Z0-9-]+)/?', login_required(views.PatientUpdateView.as_view()), name="patient_update"),
	url(r'^patient/(?P<slug>[a-zA-Z0-9-]+)/?', login_required(views.PatientDetailView.as_view()), name='patient' ),
	url(r'^new_patient', login_required(views.PatientCreateView.as_view()), name="new_patient"),
	
	# searches
    url(r'^search_dentist', views.search_dentist, name='search_dentist'),
    url(r'^search_patient', views.search_patient, name='search_patient'),
    url(r'^search_office', views.search_office, name='search_office'),

    #schedules
    url(r'^schedule/list', views.SchedulesListView.as_view(), name="schedules_list"),
    url(r'^new_schedule', login_required(views.ScheduleCreateView.as_view()), name="schedule_create"),
    url(r'^schedule/day/(?P<id>)/$', views.ScheduleDetailView.as_view(), name="schedule_detail"),
    url(r'^schedule/day_edit/(?P<id>)/$', views.ScheduleUpdateView.as_view(), name="schedule_edit"),

    #appointements

]
