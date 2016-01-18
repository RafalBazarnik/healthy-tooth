from django import forms
from . import models
from django.contrib.admin import widgets 
from functools import partial
from django.utils.text import slugify


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
        fields = ['name', 'surname', 'pesel', 'sex', 'age', 'slug', 'phone_number', 'phone_number_alt',
                  'email', 'province', 'city', 'street', 'number',]

    def __init__(self, *args, **kwargs):
        super(NewPatientForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages['required'] = 'Proszę podać imię pacjenta!'
        self.fields['surname'].error_messages['required'] = 'Proszę podać nazwisko pacjenta!'
        self.fields['pesel'].error_messages['required'] = 'Proszę podać pesel pacjenta!'
        self.fields['sex'].error_messages['required'] = 'Proszę podać płeć pacjenta!'
        self.fields['age'].error_messages['required'] = 'Proszę podać wiek pacjenta!'
        self.fields['slug'].error_messages['required'] = 'Proszę podać SEO-link pacjenta!'
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
        fields = ['professional_title', 'name', 'surname', 'biography', 'slug', 'pwz_number', 'specialties', 'office', 'profile_image']
    
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
                  'email', 'province', 'city', 'street', 'number',]

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

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class NewScheduledDay(forms.ModelForm):
    class Meta:
        model = models.DentistDay
        widgets = {'date': DateInput(),}
        exclude = []

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('_user')
        super(NewScheduledDay, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['dentist'].queryset = models.Dentist.objects.filter(office__user=user)
            self.fields['office'].queryset = models.Office.objects.filter(user=user)