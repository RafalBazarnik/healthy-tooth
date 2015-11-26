from django.db import models
from django.core.files import File
from django_markdown.models import MarkdownField
from django.core.validators import RegexValidator
from django.core.validators import validate_email
from django.contrib.auth.models import User
import os

# Create your models here.
class Address(models.Model):
	PROVINCE = (
		("DS", "dolnośląskie"),
		("KP", "kujawsko-pomorskie"),
		("LU", "lubelskie"),
		("LB", "lubuskie"),
		("LD", "łódzkie"),
		("MA", "małopolskie"),
		("MZ", "mazowieckie"),
		("OP", "opolskie"),
		("PK", "podkarpackie"),
		("PD", "podlaskie"),
		("PM", "pomorskie"),
		("SL", "śląskie"),
		("SK", "świętokrzyskie"),
		("WN", "warmińsko-mazurskie"),
		("WP", "wielkopolskie"),
		("ZP", "zachodniopomorskie"),
	)
	province = models.CharField(choices=PROVINCE, max_length=20)
	city = models.CharField(max_length=100)
	street = models.CharField(max_length=100)
	number = models.CharField(max_length=20)

	class Meta:
		abstract = True
			
class Contact(Address):
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=20)
	phone_number_alt = models.CharField(validators=[phone_regex], blank=True, max_length=20)
	email = models.EmailField()

	class Meta:
		abstract = True

def get_image_path(instance, filename):
	return os.path.join('photos', str(filename))

class Patient(models.Model):
	
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	pesel = models.CharField(max_length=11, null=True)
	slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

	def __str__(self):
		return self.surname + self.name

	def get_absolute_url(self):
		return "/patient/{0}/".format(self.slug)

	class Meta:
		verbose_name = "Our Patient"
		verbose_name_plural = 'Our Patients'


class Event(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateTimeField()
	text = MarkdownField()
	subject = models.ForeignKey(Patient, blank=True, null=True)
	slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "patient/{0}/{1}/".format(self.subject.slug, self.slug)

	class Meta:
		verbose_name = "Event"
		verbose_name_plural = 'Events'

class Office(Contact):
	name = models.CharField(max_length=150)
	office_id = models.CharField(max_length=10, unique=True, null=False, blank=False)
	slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "office/{0}/".format(self.slug)

	class Meta:
		verbose_name = "Office"
		verbose_name_plural = 'Offices'


class Dentist(models.Model):
	title = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	biography = models.CharField(max_length=5000)
	profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	pwz_number = models.CharField(max_length=87, null=True, help_text="7-cyfrowy numer prawa wykonywania zawodu (PWZ)")
	slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

	def __str__(self):
		return self.surname + self.name

	def get_absolute_url(self):
		return "dentist/{0}/".format(self.slug)

	class Meta:
		verbose_name = "Dentist"
		verbose_name_plural = 'Dentists'
