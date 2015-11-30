from django.db import models
from django.core.files import File
from django_markdown.models import MarkdownField
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.validators import validate_email
from django.contrib.auth.models import User
import os

# Create your models here.
class Address(models.Model):
	PROVINCE = [
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
	]
	province = models.CharField(choices=PROVINCE, null=True, max_length=20, help_text="Województwo")
	city = models.CharField(max_length=100, null=True)
	street = models.CharField(max_length=100, null=True)
	number = models.CharField(max_length=20, null=True, help_text="Numer domu/mieszkania")

	def province_verbose(self):
		return dict(Address.PROVINCE)[self.province]

	class Meta:
		abstract = True
			
class Contact(Address):
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15, help_text="Numer telefonu")
	phone_number_alt = models.CharField(validators=[phone_regex], blank=True, max_length=15, help_text="Alternatywny numer telefonu")
	email = models.EmailField(null=True)

	class Meta:
		abstract = True

def get_image_path(instance, filename):
	return os.path.join('photos', str(filename))

class Patient(Contact):
	SEX = [
		("F", "kobieta"),
		("M", "mężczyzna"),
	]
	name = models.CharField(max_length=100, help_text="Imię")
	surname = models.CharField(max_length=100, help_text="Nazwisko")
	pesel = models.CharField(max_length=11, null=True, help_text="Numer PESEL", validators=[MaxLengthValidator(11), MinLengthValidator(11)])
	sex = models.CharField(choices=SEX, null=True, max_length=20, help_text="Płeć")
	age = models.CharField(null=True, max_length=3, help_text="Wiek")
	slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

	# def save(self, *args, **kwargs):
	#     if not self.subject_init:
	#         self.age = self.calculate_age_from_pesel(self.pesel)
	#     super(Patient, self).save(*args, **kwargs)

	def __str__(self):
		return self.surname + self.name

	def get_absolute_url(self):
		return "/patient/{0}/".format(self.slug)

	def province_verbose(self):
		return dict(Address.PROVINCE)[self.province]

	def calculate_age_from_pesel(pesel):
		year = int(pesel[0:2])
		month = int(pesel[2:4])
		day = int(pesel[4:6])

	class Meta:
		verbose_name = "Our Patient"
		verbose_name_plural = 'Our Patients'

class Dentist(models.Model):
	professional_title = models.CharField(max_length=50, help_text="Tytuł zawodowy dentysty")
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	biography = models.CharField(max_length=5000)
	profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	pwz_number = models.CharField(max_length=87, null=True, help_text="7-cyfrowy numer prawa wykonywania zawodu (PWZ)",
		 validators=[MaxLengthValidator(7), MinLengthValidator(7)])
	specialties = models.CharField(max_length=50, null=True, help_text="Specjalizacja")
	slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

	def __str__(self):
		return self.surname + self.name

	def get_absolute_url(self):
		return "dentist/{0}/".format(self.slug)

	class Meta:
		verbose_name = "Dentist"
		verbose_name_plural = 'Dentists'

class Event(models.Model):
	EVENT_TYPES = [
		("A1", "wizyta kontrolna"),
		("A2", "leczenie kanałowe"),
		("A3", "plombowanie"),
		("A4", "inne"),
	]
	title = models.CharField(max_length=100, null=True)
	date = models.DateTimeField()
	event_type = models.CharField(choices=EVENT_TYPES, default="A4", max_length=20, help_text="Rodzaj wizyty")
	text = MarkdownField()
	subject = models.ForeignKey(Patient, blank=True, null=True)
	office = models.ForeignKey(Office, blank=True, null=True)
	dentist = models.ForeignKey(Dentist, blank=True, null=True)
	slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "patient/{0}/{1}/".format(self.subject.slug, self.slug)

	def event_type_verbose(self):
		return dict(Event.EVENT_TYPES)[self.event_type]

	class Meta:
		verbose_name = "Event"
		verbose_name_plural = 'Events'

class Office(Contact):
	user = models.OneToOneField(User, blank=True, null=True)
	name = models.CharField(max_length=150)
	office_id = models.CharField(max_length=10, unique=True, null=False, blank=False, help_text="Indywidualna nazwa kodowa gabinetu")
	text = MarkdownField(null=True, help_text="Informacje o gabiencie")
	price_list = MarkdownField(null=True, help_text="Cennik")
	slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
	dentists = models.ManyToManyField(Dentist, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "office/{0}/".format(self.slug)

	class Meta:
		verbose_name = "Office"
		verbose_name_plural = 'Offices'