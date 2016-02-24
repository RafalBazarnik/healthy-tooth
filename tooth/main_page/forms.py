from django import forms
from . import models
from django.contrib.admin import widgets 
from functools import partial
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import send_mail
from django.utils.text import slugify
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.conf import settings
from .widgets import ReadOnlyWidget
import re
import datetime


DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = models.Event
        widgets = {'date': DateInput(),}
        exclude = []

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(EventCreateForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['dentist'].queryset = models.Dentist.objects.filter(office__user=user)
            self.fields['office'].initial = models.Office.objects.get(user=user)
            self.fields['office'].queryset = models.Office.objects.filter(user=user)
            self.fields['date'].initial = datetime.date.today()

class UserAppointementEditForm(forms.ModelForm):
    class Meta:
        model = models.DentistDay
        widgets = {'date': DateInput(),}
        exclude = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')

        super(UserAppointementEditForm, self).__init__(*args, **kwargs)
        self.fields['office'].queryset = models.Office.objects.filter(user=self.user)
        self.fields['dentist'].queryset = models.Dentist.objects.filter(office__user=self.user)
        
class UserAppointementSignUpForm(forms.ModelForm):
    class Meta:
        model = models.DentistDay
        exclude = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.request = kwargs.pop('request')

        super(UserAppointementSignUpForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.HiddenInput()
        self.fields['office'].widget = forms.HiddenInput()
        self.fields['dentist'].widget = forms.HiddenInput()

        if not getattr(self.instance, 'slot10_11') or not getattr(self.instance, 'slot10_11') == getattr(self.instance, 'office').user or "Patients" in getattr(self.instance, 'slot10_11').groups.all():
            self.fields['slot10_11'].widget = forms.HiddenInput()
        else:
            self.fields['slot10_11'].queryset = models.User.objects.filter(id=self.user.id) 
        if not getattr(self.instance, 'slot11_12') or not getattr(self.instance, 'slot11_12') == getattr(self.instance, 'office').user or "Patients" in getattr(self.instance, 'slot11_12').groups.all():
            self.fields['slot11_12'].widget = forms.HiddenInput()
        else:
            self.fields['slot11_12'].queryset = models.User.objects.filter(id=self.user.id)
        if not getattr(self.instance, 'slot12_13') or not getattr(self.instance, 'slot12_13') == getattr(self.instance, 'office').user or "Patients" in getattr(self.instance, 'slot12_13').groups.all():
            self.fields['slot12_13'].widget = forms.HiddenInput()
        else:
            self.fields['slot12_13'].queryset = models.User.objects.filter(id=self.user.id) 
        if not getattr(self.instance, 'slot13_14') or not getattr(self.instance, 'slot13_14') == getattr(self.instance, 'office').user or "Patients" in getattr(self.instance, 'slot13_14').groups.all():
            self.fields['slot13_14'].widget = forms.HiddenInput()
        else:
            self.fields['slot13_14'].queryset = models.User.objects.filter(id=self.user.id)
        if not getattr(self.instance, 'slot14_15') or not getattr(self.instance, 'slot14_15') == getattr(self.instance, 'office').user or "Patients" in getattr(self.instance, 'slot14_15').groups.all():
            self.fields['slot14_15'].widget = forms.HiddenInput()
        else:
            self.fields['slot14_15'].queryset = models.User.objects.filter(id=self.user.id)
        if not getattr(self.instance, 'slot15_16') or not getattr(self.instance, 'slot15_16') == getattr(self.instance, 'office').user or "Patients" in getattr(self.instance, 'slot15_16').groups.all():
            self.fields['slot15_16'].widget = forms.HiddenInput()
        else:
            self.fields['slot15_16'].queryset = models.User.objects.filter(id=self.user.id)
        if not getattr(self.instance, 'slot16_17') or not getattr(self.instance, 'slot16_17') == getattr(self.instance, 'office').user or "Patients" in getattr(self.instance, 'slot16_17').groups.all():
            self.fields['slot16_17'].widget = forms.HiddenInput()
        else:
            self.fields['slot16_17'].queryset = models.User.objects.filter(id=self.user.id) 
        if not getattr(self.instance, 'slot17_18') or not getattr(self.instance, 'slot17_18') == getattr(self.instance, 'office').user or "Patients" in getattr(self.instance, 'slot17_18').groups.all():
            self.fields['slot17_18'].widget = forms.HiddenInput()
        else:
            self.fields['slot17_18'].queryset = models.User.objects.filter(id=self.user.id)
        if not getattr(self.instance, 'slot18_19') or not getattr(self.instance, 'slot18_19') == getattr(self.instance, 'office').user or "Patients" in getattr(self.instance, 'slot18_19').groups.all():
            self.fields['slot18_19'].widget = forms.HiddenInput()
        else:
            self.fields['slot18_19'].queryset = models.User.objects.filter(id=self.user.id) 
        if not getattr(self.instance, 'slot19_20') or not getattr(self.instance, 'slot19_20') == getattr(self.instance, 'office').user or "Patients" in getattr(self.instance, 'slot19_20').groups.all():
            self.fields['slot19_20'].widget = forms.HiddenInput()
        else:
            self.fields['slot19_20'].queryset = models.User.objects.filter(id=self.user.id)

    def clean_date(self):
        return getattr(self.instance, 'date')

    def clean_office(self):
        return getattr(self.instance, 'office')

    def clean_dentist(self):
        return getattr(self.instance, 'dentist')

class UserAppointmentCancelForm(forms.ModelForm):
    class Meta:
        model = models.DentistDay
        exclude = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.request = kwargs.pop('request')
        super(UserAppointmentCancelForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.HiddenInput()
        self.fields['dentist'].widget = forms.HiddenInput()
        self.fields['office'].widget = forms.HiddenInput()
        self.fields['slot10_11'].widget = forms.HiddenInput()
        self.fields['slot11_12'].widget = forms.HiddenInput()
        self.fields['slot12_13'].widget = forms.HiddenInput()
        self.fields['slot13_14'].widget = forms.HiddenInput()
        self.fields['slot14_15'].widget = forms.HiddenInput()
        self.fields['slot15_16'].widget = forms.HiddenInput()
        self.fields['slot16_17'].widget = forms.HiddenInput()
        self.fields['slot17_18'].widget = forms.HiddenInput()
        self.fields['slot18_19'].widget = forms.HiddenInput()
        self.fields['slot19_20'].widget = forms.HiddenInput()

    def save(self, *args, **kwargs):
        instance = super(UserAppointmentCancelForm, self).save(commit=False)
        office = instance.office.user
        fields = instance._meta.get_fields()
        for field in fields:
            if getattr(instance, field.name) is not None:
                if getattr(instance, field.name) == self.user:
                    setattr(instance, field.name, office) 
        instance.save()
        messages.add_message(self.request, messages.INFO, 'Anulowano wizytę!')
        return instance

class UserContactInfoChangeForm(forms.ModelForm):
    pass


class UserPasswordChangeForm(forms.Form):
    password1 = forms.CharField(label='Nowe hasło', widget=forms.PasswordInput,)
    password2 = forms.CharField(label='Powtórz nowe hasło', widget=forms.PasswordInput,)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)

    def clean_new_password(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(self.error_messages['Hasła muszą się zgadzać!'],code=['passwords_doesnt_match'])
        if len(password1) < 6:
            raise forms.ValidationError(self.error_messages['Hasło zbyt krótkie. Minimalna długość hasła to 6'], code=['password_too_short'])
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['password1'])
        if commit:
            User.objects.filter(pk=self.user.id).update(password=self.user.password,)
        return self.user

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': ' Imię i Nazwisko'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': ' Email'}))
    contact_phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': ' Telefon'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': ' Wiadomość'}))
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].error_messages['required'] = 'Proszę podać swoje imię i nazwisko!'
        self.fields['contact_email'].error_messages['required'] = 'Proszę podać adres email do kontaku zwrotnego!'
        self.fields['contact_phone'].error_messages['required'] = 'Proszę podać numer telefonu do kontaku zwrotnego!'
        self.fields['content'].error_messages['required'] = 'Treść wiadomości nie powinna być pusta!'


class NewPatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = ['name', 'surname', 'pesel', 'sex', 'age', 'phone_number', 'phone_number_alt',
                  'email', 'province', 'city', 'street', 'number', 'profile_image']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(NewPatientForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages['required'] = 'Proszę podać imię pacjenta!'
        self.fields['surname'].error_messages['required'] = 'Proszę podać nazwisko pacjenta!'
        self.fields['pesel'].error_messages['required'] = 'Proszę podać pesel pacjenta!'
        self.fields['sex'].error_messages['required'] = 'Proszę podać płeć pacjenta!'
        self.fields['age'].error_messages['required'] = 'Proszę podać wiek pacjenta!'
        self.fields['phone_number'].error_messages['required'] = 'Proszę podać nr telefonu pacjenta!'
        self.fields['phone_number'].error_messages['invalid'] = 'Proszę podać nr telefonu pacjenta!'
        self.fields['phone_number_alt'].error_messages['required'] = 'Proszę podać nr telefonu pacjenta!'
        self.fields['email'].error_messages['required'] = 'Proszę podać adres email pacjenta!'
        self.fields['province'].error_messages['required'] = 'Proszę podać województwo!'
        self.fields['city'].error_messages['required'] = 'Proszę podać miejscowość!'
        self.fields['street'].error_messages['required'] = 'Proszę podać ulicę!'
        self.fields['number'].error_messages['required'] = 'Proszę podać numer domu/mieszkania!'

class NewDentistForm(forms.ModelForm):
    class Meta:
        model = models.Dentist
        fields = ['professional_title', 'name', 'surname', 'biography', 'pwz_number', 'specialties', 'office', 'profile_image']
    
    def __init__(self, *args, **kwargs):
        super(NewDentistForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages['required'] = 'Proszę podać imię dentysty!'
        self.fields['surname'].error_messages['required'] = 'Proszę podać imię dentysty!'
        self.fields['professional_title'].error_messages['required'] = 'Proszę podać tytuł dentysty!'
        self.fields['biography'].error_messages['required'] = 'Proszę wprowadzic biografię zawodową dentysty!'
        self.fields['pwz_number'].error_messages['required'] = 'Proszę podać numer uprawnienia do zawodu lekarze (PWZ) dentysty!'
        self.fields['specialties'].error_messages['required'] = 'Proszę podać specjalności zawodowe dentysty!'
        self.fields['office'].error_messages['required'] = 'Proszę podać gabinet w którym pracuje dentysta!'
        

class NewOfficeForm(forms.ModelForm):
    class Meta:
        model = models.Office
        fields = ['text', 'price_list', 'phone_number', 'phone_number_alt',
                  'email', 'province', 'city', 'street', 'number', 'logo_image']

    def __init__(self, *args, **kwargs):
        super(NewOfficeForm, self).__init__(*args, **kwargs)
        self.fields['text'].error_messages['required'] = 'Proszę podać opis gabinetu!'
        self.fields['price_list'].error_messages['required'] = 'Proszę podać listę cen usług gabinetu!'
        self.fields['phone_number'].error_messages['required'] = 'Proszę podać nr telefonu gabinetu!'
        self.fields['phone_number'].error_messages['invalid'] = 'Proszę podać nr telefonu pacjenta!'
        self.fields['phone_number_alt'].error_messages['required'] = 'Proszę podać nr telefonu gabinetu!'
        self.fields['email'].error_messages['required'] = 'Proszę podać adres email gabinetu!'
        self.fields['province'].error_messages['required'] = 'Proszę podać województwo!'
        self.fields['city'].error_messages['required'] = 'Proszę podać miejscowość!'
        self.fields['street'].error_messages['required'] = 'Proszę podać ulicę!'
        self.fields['number'].error_messages['required'] = 'Proszę podać numer domu/mieszkania!'

class NewAppointmentForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = ['name', 'surname', 'phone_number', 'phone_number_alt', 'email', 'skype', 'preferred_date',
                  'preferred_date_alt' , 'preferred_date_alt2' , 'extra_info', 'office', 
                  'personal_data_agreement',]

class UpdateAppointmentForm(NewAppointmentForm):
    pass

class NewScheduledDay(forms.ModelForm):
    class Meta:
        model = models.DentistDay
        widgets = {'date': DateInput(),}
        exclude = []

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(NewScheduledDay, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['dentist'].queryset = models.Dentist.objects.filter(office__user=user)
            self.fields['office'].queryset = models.Office.objects.filter(user=user)
            self.fields['date'].initial = datetime.date.today()