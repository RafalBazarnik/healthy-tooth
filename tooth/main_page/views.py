from django.views import generic
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.views.generic import TemplateView
from .forms import ContactForm
from django.utils.text import slugify
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib import messages
from django.core.urlresolvers import reverse
from braces.views import GroupRequiredMixin, LoginRequiredMixin
from . import models, forms
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import send_mail


#office
class EventCreateView(CreateView):
    model = models.Event
    template_name = 'office/new_event.html'
    form_class = forms.EventCreateForm

    def get_form_kwargs(self):
        kwargs = super(EventCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(EventCreateView, self).dispatch(*args, **kwargs)

#login_required
class EventDetailView(generic.DetailView):
    model = models.Event
    template_name = 'patient/event_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventDetailView, self).dispatch(*args, **kwargs)

#patient
class UserEventsView(generic.ListView):
    model = models.Patient
    template_name = "patient/patient_history.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super(UserEventsView, self).get_queryset().filter(user=self.request.user)
        return queryset

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Patients').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(UserEventsView, self).dispatch(*args, **kwargs)

#patients
class UserPersonalDataView(generic.ListView):
    queryset = models.Patient.objects.all()
    model = models.Patient
    template_name = "patient/patient_info.html"

    def get_queryset(self):
        queryset = super(UserPersonalDataView, self).get_queryset().filter(user=self.request.user)
        return queryset

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Patients').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(UserPersonalDataView, self).dispatch(*args, **kwargs)

#patient
class UserAppointementSignUpView(UpdateView):
    model = models.DentistDay
    template_name = "patient/patient_signup_appointment.html"
    form_class = forms.UserAppointementSignUpForm

    def get_success_url(self):
        return reverse('main_page:patient_appointements')

    def get_form_kwargs(self):
        kwargs = super(UserAppointementSignUpView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        dday_pk = self.get_object().pk
        context = super(UserAppointementSignUpView, self).get_context_data(**kwargs)
        context['dday'] = models.DentistDay.objects.filter(pk=dday_pk)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserAppointementSignUpView, self).dispatch(*args, **kwargs)

#patient
class PatientInfoView(generic.DetailView):
    model = models.Patient
    template_name = 'patient/patient_info.html'

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Patients').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PatientInfoView, self).dispatch(*args, **kwargs)

#patient
class PatientHistoryView(generic.DetailView):
    model = models.Patient
    template_name = 'patient/patient_history.html'

    def get_context_data(self, **kwargs):
        patient = self.get_object().pk
        context = super(PatientHistoryView, self).get_context_data(**kwargs)
        context['events'] = models.Event.objects.filter(subject=patient).order_by('date')
        return context

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Patients').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PatientHistoryView, self).dispatch(*args, **kwargs)

#patient
class PatientAppointmentsCancelView(generic.UpdateView):
    model = models.DentistDay
    template_name = "patient/patient_cancel_appointments.html"
    form_class = forms.UserAppointmentCancelForm

    def get_success_url(self):
        return reverse('main_page:patient_appointements')

    def get_form_kwargs(self):
        kwargs = super(PatientAppointmentsCancelView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['request'] = self.request
        return kwargs

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Patients').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PatientAppointmentsCancelView, self).dispatch(*args, **kwargs)

#patient
class PatientAppointmentsView(generic.ListView):
    queryset = models.DentistDay.objects.all().order_by('date')
    template_name = "patient/patient_appointements.html"
    paginate_by = 10

    def get_queryset(self):
        user_id = self.request.user.id
        object_list = super(PatientAppointmentsView, self).get_queryset()
        return object_list.filter(Q(slot10_11=user_id) | Q(slot11_12=user_id) | Q(slot12_13=user_id) |
            Q(slot13_14=user_id) | Q(slot14_15=user_id) | Q(slot15_16=user_id) | Q(slot16_17=user_id) |
            Q(slot17_18=user_id) | Q(slot18_19=user_id) | Q(slot19_20=user_id)).order_by('date')

    def get_form_kwargs(self):
        kwargs = super(PatientAppointmentsView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Patients').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PatientAppointmentsView, self).dispatch(*args, **kwargs)

#open
class PatientCreateView(CreateView):
    model = models.Patient
    template_name = 'patient/new_patient.html'
    form_class = forms.NewPatientForm

    def get_success_url(self):
        if self.request.user.groups.all() and self.request.user.groups.all()[0].name == "Offices":
            return reverse('main_page:patients')
        else:
            return reverse('main_page:login_user')

    def form_valid(self, form):
        if self.request.user.groups.all() and self.request.user.groups.all()[0].name == "Offices":
            messages.add_message(self.request, messages.INFO, 'Konto zostało utworzone. Na skrzynkę mailową pacjenta została wysłana wiadomość z loginem i hasłem')
        else:
            messages.add_message(self.request, messages.INFO, 'Konto zostało utworzone. Na skrzynkę mailową została wysłana wiadomość z loginem i hasłem')
        return super(PatientCreateView, self).form_valid(form)

#office
class SchedulesListView(generic.ListView):
    queryset = models.DentistDay.objects.all()
    template_name = "office/dentist_schedules_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        context = super(SchedulesListView, self).get_context_data(**kwargs)
        context['dentists'] = models.Dentist.objects.filter(office__user_id=user_id)
        return context

    def get_queryset(self):
        user_id = self.request.user.id
        object_list = super(SchedulesListView, self).get_queryset()
        return object_list.filter(office__user_id=user_id).order_by('date')

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(SchedulesListView, self).dispatch(*args, **kwargs)

#office
class ScheduleCreateView(CreateView):
    model = models.DentistDay
    template_name = 'office/new_dentist_schedule.html'
    form_class = forms.NewScheduledDay

    def get_form_kwargs(self):
        kwargs = super(ScheduleCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(ScheduleCreateView, self).dispatch(*args, **kwargs)

#office
class ScheduleUpdateView(UpdateView):
    model = models.DentistDay
    template_name = 'office/new_dentist_schedule.html'
    form_class = forms.UserAppointementEditForm

    def get_form_kwargs(self):
        kwargs = super(ScheduleUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(ScheduleUpdateView, self).dispatch(*args, **kwargs)

#open
class ScheduleDetailView(generic.DetailView):
    model = models.DentistDay
    template_name = 'office/schedule_detail.html'

#open
class ScheduleInstructionView(TemplateView):
    template_name = 'office/schedule_instruction.html'

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Patients').count() == 1, login_url='/forbidden')
def patient_index(request):
    context = RequestContext(request)
    return render(request, 'patient/patient_index.html', context)

#open
def login_user(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if user.groups.filter(name="Offices").exists():
                    return HttpResponseRedirect('/account/')
                elif user.groups.filter(name="Patients").exists():
                    return HttpResponseRedirect('/patient_zone')
                else:
                    return HttpResponseRedirect('/')
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

@login_required
def password_change(request):
    context = RequestContext(request)
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = authenticate(username=request.user.username, password=old_password)
        if user:
            if password1 != password2:
                messages.add_message(request, messages.WARNING, "Hasła muszą się zgadzać!")
                return render(request, 'patient/change_password.html', {}, context)
            else:
                if len(password1) < 5:
                    messages.add_message(request, messages.WARNING, "Hasło zbyt krótkie. Minimalna długość hasła to 5")
                    return render(request, 'patient/change_password.html', {}, context)
                else:
                    user.set_password(password2)
                    user.save()
                    messages.add_message(request, messages.WARNING, "Poprawnie zmieniono hasło")
                    return render(request, 'login.html', {}, context)
        else:
            messages.add_message(request, messages.WARNING, "Niepoprawne stare hasło!")
            return render(request, 'patient/change_password.html', {}, context)

    else:
        return render(request, 'patient/change_password.html', {}, context)

#open
def password_reset(request):
    context = RequestContext(request)
    if request.method == 'POST':
        login = request.POST.get('login')
        email = request.POST.get('email')
        if User.objects.filter(username = login).count() == 1:
            user = User.objects.get(username=login)
            if user.email == email:
                password = User.objects.make_random_password()
                user.set_password(password)
                user.save()
                message_text = "Twoje hasło w serwisie Ząbek zostało zmienione. Twoje hasło to: {0}.".format(password)
                send_mail(
                    subject="reset hasła w serwisie Ząbek",
                    message=message_text,
                    from_email='bazarnik.rafal@gmail.com',
                    recipient_list=[email],
                    fail_silently=False
                )
                messages.add_message(request, messages.ERROR, "Twoje nowe hasło zostało wysłane na podany adres email")
                return render(request, 'login.html', {}, context)
            else:
                messages.add_message(request, messages.ERROR, "Twoje konto ma przypisany inny adres email")
                return render(request, 'password_reset.html', {}, context)
        else:
            messages.add_message(request, messages.ERROR, "Nie istnieje w bazie taki użytkownik")
            return render(request, 'password_reset.html', {}, context)
    else:
        return render(request, 'password_reset.html', {}, context)

#open
class IndexView(TemplateView):
    template_name = "index.html"

#open
class AboutView(TemplateView):
    template_name = "about.html"

#office
class PatientsListView(generic.ListView):
    queryset = models.Patient.objects.all()
    template_name = "patient/patients_list.html"
    paginate_by = 10

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PatientsListView, self).dispatch(*args, **kwargs)

#office
class PatientDetailView(generic.DetailView):
    model = models.Patient
    template_name='patient/patient_detail.html'

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PatientDetailView, self).dispatch(*args, **kwargs)

#office
class PatientUpdateView(UpdateView):
    model = models.Patient
    template_name = 'patient/new_patient.html'
    form_class = forms.NewPatientForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PatientUpdateView, self).dispatch(*args, **kwargs)

#open
class DentistsListView(generic.ListView):
    queryset = models.Dentist.objects.all()
    template_name = "dentist/dentists_list.html"
    paginate_by = 25

#open
class DentistDetailView(generic.DetailView):
    model = models.Dentist
    template_name='dentist/dentist_detail.html'

    def get_context_data(self, **kwargs):
        dentist = self.get_object().pk
        context = super(DentistDetailView, self).get_context_data(**kwargs)
        context['schedules'] = models.DentistDay.objects.filter(dentist_id=dentist).order_by('date')
        return context

#office
class DentistCreateView(CreateView):
    model = models.Dentist
    template_name = 'dentist/new_dentist.html'
    form_class = forms.NewDentistForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(DentistCreateView, self).dispatch(*args, **kwargs)

#office
class DentistUpdateView(UpdateView):
    model = models.Dentist
    template_name = 'dentist/new_dentist.html'
    form_class = forms.NewDentistForm

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(DentistUpdateView, self).dispatch(*args, **kwargs)

#open
class OfficesListView(generic.ListView):
    queryset = models.Office.objects.all()
    template_name = "office/offices_list.html"
    paginate_by = 25

#open
class OfficeDetailView(generic.DetailView):
    model = models.Office
    template_name='office/office_detail.html'

    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        context = super(OfficeDetailView, self).get_context_data(**kwargs)
        context['schedules'] = models.DentistDay.objects.order_by('date')
        return context

#office
class OfficeUpdateView(UpdateView):
    model = models.Office
    template_name='office/new_office.html'
    form_class = forms.NewOfficeForm

    def get_queryset(self):
        object_list = super(OfficeUpdateView, self).get_queryset()
        return object_list.filter(user=self.request.user)

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(OfficeUpdateView, self).dispatch(*args, **kwargs)

#office
class OfficeIndexView(generic.ListView):
    queryset = models.Office.objects.all()
    template_name = "office/office_index.html"
    paginate_by = 2

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(OfficeIndexView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        object_list = super(OfficeIndexView, self).get_queryset()
        return object_list.filter(user=self.request.user.id)

#open
class AccessForbiddenView(TemplateView):
    template_name = "forbidden.html"

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
            messages.add_message(request, messages.INFO, 'Wiadomość została wysłana! Postaramy się odpowiedzieć jak najszybciej - maksymalnie do 10 dni roboczych')
            return redirect('main_page:contact')
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
