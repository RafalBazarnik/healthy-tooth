from django import forms
from . import models


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)


class NewPatientForm(forms.ModelForm):
	
	class Meta:
		model = models.Patient
		fields = ('name', 'surname', 'pesel', 'slug', 'phone_number', 'phone_number_alt', 'email', 'province', 'city', 'street', 'number')
		# TODO: slug issue - no autopopulate