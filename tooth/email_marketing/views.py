from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
import main_page
from . import models, forms


# Create your views here.
class NewMarketingEmail(generic.CreateView):
    model = models.MarketingEmail
    form_class = forms.NewMarketingEmailForm
    template_name = 'email_marketing/new_email.html'

    def get_success_url(self):
        return reverse('email_marketing:emails_list')

    def get_form_kwargs(self):
        kwargs = super(NewMarketingEmail, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = form.cleaned_data.get('user')
        city_1 = form.cleaned_data.get('email_city')
        city_2 = form.cleaned_data.get('email_city_alt1')
        city_3 = form.cleaned_data.get('email_city_alt2')
        sex = form.cleaned_data.get('email_patients_sex')
        patients = main_page.models.Patient.objects.all()
        if city_2 and city_3:
            patients = patients.filter(Q(city=city_1) | Q(city=city_2) | Q(city=city_3))
        elif city_2:
            patients = patients.filter(Q(city=city_1) | Q(city=city_2))
        elif city_3:
            patients = patients.filter(Q(city=city_1) | Q(city=city_3))
        else:
            patients = patients.filter(Q(city=city_1))
        if sex:
            patients = patients.filter(Q(sex=sex))
        patients = patients.values_list('email', flat=True)
        receivers_list = []
        receivers_list.append(user.email)
        receivers_list.append("aziwsti@gmail.com")
        for email in patients:
            receivers_list.append(email)
        mail = EmailMessage(form.cleaned_data.get('email_title'), form.cleaned_data.get('email_text'), from_email='user.email', bcc=receivers_list)
        # send_mail(
        #     subject=form.cleaned_data.get('email_title'),
        #     message=form.cleaned_data.get('email_text'),
        #     from_email=user.email,
        #     bcc=receivers_list,
        #     fail_silently=False
        #     )
        mail.send(fail_silently=False)
        receivers_string = ', '.join(receivers_list)
        send_mail(
            subject="Raport z wysłania wiadomości marketingowej",
            message="Wiadomość wysłano do: {}".format(receivers_string),
            from_email="aziwsti@gmail.com",
            recipient_list=[user.email, 'bazarnik.rafal@gmail.com',],
            fail_silently=False
            )
        return super(NewMarketingEmail, self).form_valid(form)

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(NewMarketingEmail, self).dispatch(*args, **kwargs)


class MarketingEmailList(generic.ListView):
    queryset = models.MarketingEmail.objects.all()
    template_name = "email_marketing/emails_list.html"
    paginate_by = 12

    def get_queryset(self):
        queryset = super(MarketingEmailList, self).get_queryset().filter(user=self.request.user).order_by('email_date')
        return queryset

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(MarketingEmailList, self).dispatch(*args, **kwargs)


class MarketingEmailDetail(generic.DetailView):
    model = models.MarketingEmail
    template_name = "email_marketing/email_detail.html"

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(MarketingEmailDetail, self).dispatch(*args, **kwargs)
