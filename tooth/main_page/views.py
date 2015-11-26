from django.views import generic
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext
from django.views.generic import TemplateView
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from . import models

class IndexView(TemplateView):
	template_name = "index.html"

class AboutView(TemplateView):
	template_name = "about.html"

class PatientsListView(generic.ListView):
	queryset = models.Patient.objects.all()
	template_name = "patients_list.html"
	paginate_by = 25

class DentistsListView(generic.ListView):
	queryset = models.Dentist.objects.all()
	template_name = "dentists_list.html"
	paginate_by = 25

class OfficesListView(generic.ListView):
	queryset = models.Office.objects.all()
	template_name = "offices_list.html"
	paginate_by = 25

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
