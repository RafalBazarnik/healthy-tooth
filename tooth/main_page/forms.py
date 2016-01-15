from django import forms
from . import models
from django.contrib.admin import widgets 
from functools import partial


class ContactForm(forms.Form):
	# CHOICES = (
	# 	(1, "Przystąpienie do franczyzy"),
	# 	(2, "Kontakty z prasą"),
	# 	(3, "Uwagi co do strony internetowej"),
	# 	(4, "Reklamacje"),
	# 	(5, "Inne")
	# )	
	contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': ' Imię i Nazwisko'}))
	contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': ' Email'}))
	contact_phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': ' Telefon'}))
	# contact_topic = forms.ChoiceField(choices=CHOICES , initial='', widget=forms.Select(attrs={'data-placeholder': 'Temat wiadomości'}), required=True)
	content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': ' Wiadomość'}))

class NewPatientForm(forms.ModelForm):
	class Meta:
		model = models.Patient
		fields = ['name', 'surname', 'pesel', 'sex', 'age', 'slug', 'phone_number', 'phone_number_alt',
				  'email', 'province', 'city', 'street', 'number',]

class NewDentistForm(forms.ModelForm):
	class Meta:
		model = models.Dentist
		fields = ['professional_title', 'name', 'surname', 'biography', 'slug', 'pwz_number', 'specialties', 'office']

class NewOfficeForm(forms.ModelForm):
	class Meta:
		model = models.Office
		fields = ['text', 'price_list', 'phone_number', 'phone_number_alt',
				  'email', 'province', 'city', 'street', 'number',]

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

	def __init__(self, user, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(NewScheduledDay, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['dentist'].queryset = models.Dentist.objects.filter(office__user=self.user)
			self.fields['office'].queryset = models.Office.objects.filter(user=self.user)