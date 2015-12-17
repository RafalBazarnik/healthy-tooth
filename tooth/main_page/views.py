from django.views import generic
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext
from django.views.generic import TemplateView
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from . import models, forms
from django.utils.safestring import mark_safe


def login_user(request):
	context =RequestContext(request)
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/account/')
			else:
				messages.add_message(request, messages.WARNING, "Twoje konto zostało zablokowane, skontaktuj się z administratorem!")
				return render(request, 'login.html', {}, context)
		else:
			messages.add_message(request, messages.ERROR, "Błędny login lub hasło!")
			return render(request, 'login.html', {}, context)
	else:
		return render(request, 'login.html', {}, context)

@login_required
def logout_user(request):
	context = RequestContext(request)
	logout(request)
	return HttpResponseRedirect('/')

class IndexView(TemplateView):
	template_name = "index.html"

class AboutView(TemplateView):
	template_name = "about.html"

class PatientsListView(generic.ListView):
	queryset = models.Patient.objects.all()
	template_name = "patient/patients_list.html"
	paginate_by = 25

class PatientDetailView(generic.DetailView):
	model = models.Patient
	template_name='patient/patient_detail.html'

class PatientCreateView(CreateView):
	model = models.Patient
	template_name = 'patient/new_patient.html'
	form_class = forms.NewPatientForm

class PatientUpdateView(UpdateView):
	model = models.Patient
	template_name = 'patient/new_patient.html'
	form_class = forms.NewPatientForm

class DentistsListView(generic.ListView):
	queryset = models.Dentist.objects.all()
	template_name = "dentist/dentists_list.html"
	paginate_by = 25

class DentistDetailView(generic.DetailView):
	model = models.Dentist
	template_name='dentist/dentist_detail.html'

class DentistCreateView(CreateView):
	model = models.Dentist
	template_name = 'dentist/new_dentist.html'
	form_class = forms.NewDentistForm

class DentistUpdateView(UpdateView):
	model = models.Dentist
	template_name = 'dentist/new_dentist.html'
	form_class = forms.NewDentistForm

class OfficesListView(generic.ListView):
	queryset = models.Office.objects.all()
	template_name = "office/offices_list.html"
	paginate_by = 25

class OfficeDetailView(generic.DetailView):
	model = models.Office
	template_name='office/office_detail.html'

class OfficeUpdateView(UpdateView):
	model = models.Office
	template_name='office/new_office.html'
	form_class = forms.NewOfficeForm

	def get_queryset(self):
		object_list = super(OfficeUpdateView, self).get_queryset()
		return object_list.filter(user=self.request.user)

class OfficeIndexView(generic.ListView):
	queryset = models.Office.objects.all()
	template_name = "office/office_index.html"
	paginate_by = 2

	def get_queryset(self):
		object_list = super(OfficeIndexView, self).get_queryset()
		return object_list.filter(user=self.request.user)

class NewAppointmentView(CreateView):
	model = models.Appointment
	template_name = 'office/appointment.html'
	form_class = forms.NewAppointmentForm

class EditAppointmentView(UpdateView):
	model = models.Appointment
	template_name = 'office/appointment_edit.html'
	form_class = forms.NewAppointmentForm

# view for sending mail from contact form
def contact(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Wiadomość od: " + form.cleaned_data['contact_name'] + " " + form.cleaned_data['contact_phone']
			from_email = form.cleaned_data['contact_email']
			message = form.cleaned_data['content']
			try:
				send_mail(subject, message, from_email, ['bazarnik.rafal@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Nieprawidłowy nagłówek wiadomości! Proszę spróbuj ponownie!')
			return redirect('main_page:thanks')
	return render(request, "contact.html", {'form': form})

# view after succesful sent contact form
def thanks(request):
	return render_to_response('thanks.html', {}, context_instance=RequestContext(request))

# page not found
def handler404(request):
	response = render_to_response('errors/404.html', {}, context_instance=RequestContext(request))
	response.status_code = 404
	return response

# server error
def handler500(request):
	response = render_to_response('errors/500.html', {}, context_instance=RequestContext(request))
	response.status_code = 500
	return response

# permission denied
def handler403(request):
	response = render_to_response('errors/403.html', {}, context_instance=RequestContext(request))
	response.status_code = 403
	return response

# bad request
def handler400(request):
	response = render_to_response('errors/400.html', {}, context_instance=RequestContext(request))
	response.status_code = 400
	return response

def search_dentist(request):
	query = request.GET.get('q', '')
	page = request.GET.get('page', 1)
	results = models.Dentist.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query) | 
		Q(professional_title__icontains=query) | Q(specialties__icontains=query) | Q(pwz_number__icontains=query))

	pages = Paginator(results, 5)

	try:
		returned_page = pages.page(page)
	except EmptyPage:
		returned_page = pages.page(pages.num_pages)

	return render_to_response('dentist/search_result_dentists.html',
							  {'page_obj': returned_page,
							   'object_list': returned_page.object_list,
							   'search': query})

def search_patient(request):
	query = request.GET.get('q', '')
	page = request.GET.get('page', 1)
	results = models.Patient.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query) | 
		Q(pesel__icontains=query) | Q(city__icontains=query) | Q(street__icontains=query) | Q(phone_number__icontains=query) |
		Q(email__icontains=query))

	pages = Paginator(results, 5)

	try:
		returned_page = pages.page(page)
	except EmptyPage:
		returned_page = pages.page(pages.num_pages)

	return render_to_response('patient/search_result_patients.html',
							  {'page_obj': returned_page,
							   'object_list': returned_page.object_list,
							   'search': query})

def search_office(request):
	query = request.GET.get('q', '')
	page = request.GET.get('page', 1)
	results = models.Office.objects.filter(Q(name__icontains=query) | Q(office_id__icontains=query) | 
		Q(email__icontains=query) | Q(city__icontains=query) | Q(street__icontains=query) |
		Q(phone_number__icontains=query) | Q(phone_number_alt__icontains=query))

	pages = Paginator(results, 5)

	try:
		returned_page = pages.page(page)
	except EmptyPage:
		returned_page = pages.page(pages.num_pages)

	return render_to_response('office/search_result_office.html',
							  {'page_obj': returned_page,
							   'object_list': returned_page.object_list,
							   'search': query})
