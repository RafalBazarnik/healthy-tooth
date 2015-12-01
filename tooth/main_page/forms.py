from django import forms
from . import models


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
		fields = ('name', 'surname', 'pesel', 'slug', 'phone_number', 'phone_number_alt', 'email', 'province', 'city', 'street', 'number')

# class EditPatientForm(forms.)