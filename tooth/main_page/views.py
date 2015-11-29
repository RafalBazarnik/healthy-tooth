from django.views import generic
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext
from django.views.generic import TemplateView
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, Http404
from . import models

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.PSOT.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/account/')
			else:
				return HttpResponse("Twoje konto zostało zablokowane, skontaktuj się z administratorem.")
		else:
			return HttpResponse("Błędny login lub hasło")

	else:
		return render(request, 'login.html')


class IndexView(TemplateView):
	template_name = "index.html"

class AboutView(TemplateView):
	template_name = "about.html"

class PatientsListView(generic.ListView):
	queryset = models.Patient.objects.all()
	template_name = "patients_list.html"
	paginate_by = 25

class PatientDetailView(generic.DetailView):
	model = models.Patient
	template_name='patient_detail.html'

class DentistsListView(generic.ListView):
	queryset = models.Dentist.objects.all()
	template_name = "dentists_list.html"
	paginate_by = 25

class DentistDetailView(generic.DetailView):
	model = models.Dentist
	template_name='dentist_detail.html'

class OfficesListView(generic.ListView):
	queryset = models.Office.objects.all()
	template_name = "offices_list.html"
	paginate_by = 25

class OfficeDetailView(generic.DetailView):
	model = models.Office
	template_name='office_detail.html'

def contact(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['admin@example.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('thanks')
	return render(request, "contact.html", {'form': form})

def patient_new(request):
	if request.method == "POST":
		form = NewPatientForm(request.POST)
		if form.is_valid():
			patient = form.save(commit=False)
			patient.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = NewPatientForm()
	return render(request, 'patient_new.html', {'form': form})

def office_account(request):
	if not request.user.is_authenticated():
		return redirect('/login')
	else:
		return render_to_response('office_index.html', {}, context_instance=RequestContext(request))

def message_sent(request):
	return render_to_response('message_sent.html')

# page not found
def handler404(request):
	response = render_to_response('404.html', {}, context_instance=RequestContext(request))
	response.status_code = 404
	return response

# server error
def handler500(request):
	response = render_to_response('500.html', {}, context_instance=RequestContext(request))
	response.status_code = 500
	return response

# permission denied
def handler403(request):
	response = render_to_response('403.html', {}, context_instance=RequestContext(request))
	response.status_code = 403
	return response

# bad request
def handler400(request):
	response = render_to_response('400.html', {}, context_instance=RequestContext(request))
	response.status_code = 400
	return response
