from django.db import models
from django.core.files import File
from django_markdown.models import MarkdownField
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.validators import validate_email
from django.contrib.auth.models import User
import os
from datetime import datetime


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
	city = models.CharField(max_length=100, null=True, help_text="Miasto/Miejscowość")
	street = models.CharField(max_length=100, null=True, help_text="Ulica")
	number = models.CharField(max_length=20, null=True, help_text="Numer domu/mieszkania")

	def province_verbose(self):
		return dict(Address.PROVINCE)[self.province]

	class Meta:
		abstract = True
			
class Contact(Address):
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15, help_text="Numer telefonu")
	phone_number_alt = models.CharField(validators=[phone_regex], blank=True, max_length=15, help_text="Alternatywny numer telefonu")
	email = models.EmailField(null=True, help_text="Adres email")
	skype = models.CharField(max_length=50, null=True, blank=True)

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
	slug = models.SlugField(max_length=40, unique=True, blank=True, null=True,
							help_text="Nazwa linku w postaci - nazwisko-imie-pesel - male litery, bez polskich znaków")
	user = models.OneToOneField(User, null=True, blank=True)

	def save(self, force_insert=False, force_update=False):
		is_new = self.user is None
		super(Patient, self).save(force_insert, force_update)
		if is_new:
			password = self.pesel
			user = User.objects.create_user(username=self.slug, first_name=self.name, last_name=self.surname, email=self.email, password=password)
			user.save()
			user.is_superuser = False
			user.is_staff = False
			user.is_active = True
			self.user = user

	def __str__(self):
		return self.surname + self.name

	def get_absolute_url(self):
		return "/patient/{0}/".format(self.slug)

	def get_edit_url(self):
		return "/patient/update/{0}/".format(self.slug)

	def province_verbose(self):
		return dict(Address.PROVINCE)[self.province]

	class Meta:
		verbose_name = "Patient"
		verbose_name_plural = 'Patients'

class Office(Contact):
	user = models.OneToOneField(User, blank=True, null=True, related_name='office_user')
	name = models.CharField(max_length=150)
	office_id = models.CharField(max_length=10, unique=True, null=False, blank=False, help_text="Indywidualna nazwa kodowa gabinetu")
	text = MarkdownField(null=True, help_text="Informacje o gabiencie")
	price_list = MarkdownField(null=True, help_text="Cennik")
	slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "/office/{0}/".format(self.slug)

	def get_edit_url(self):
		return "/office/update/{0}/".format(self.slug)

	class Meta:
		verbose_name = "Office"
		verbose_name_plural = 'Offices'

class Dentist(models.Model):
	professional_title = models.CharField(max_length=50, help_text="Tytuł zawodowy dentysty")
	name = models.CharField(max_length=100, help_text="Imię")
	surname = models.CharField(max_length=100, help_text="Nazwisko")
	biography = MarkdownField(null=True, help_text="Biografia")
	profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True, help_text="Zdjęcie")
	pwz_number = models.CharField(max_length=87, null=True, help_text="7-cyfrowy numer prawa wykonywania zawodu (PWZ)",
		 validators=[MaxLengthValidator(7), MinLengthValidator(7)])
	specialties = models.CharField(max_length=50, null=True, help_text="Specjalizacja")
	slug = models.SlugField(max_length=40, unique=True, blank=True, null=True, help_text="Nazwa linku w postaci - nazwisko-imie-pwz - male litery, bez polskich znaków")
	office = models.ForeignKey(Office, null=True, related_name="workplace")

	def __str__(self):
		return self.surname + self.name

	def get_absolute_url(self):
		return "/dentist/{0}/".format(self.slug)

	def get_edit_url(self):
		return "/dentist/update/{0}/".format(self.slug)

	class Meta:
		verbose_name = "Dentist"
		verbose_name_plural = 'Dentists'

class Appointment(Contact):
	name = models.CharField(max_length=100, help_text="Imię")
	surname = models.CharField(max_length=100, help_text="Nazwisko")
	preferred_date = models.DateTimeField(help_text="Preferowany dzień i godzina wizyty")
	preferred_date_alt = models.DateTimeField(null=True, blank=True, help_text="Preferowany dzień i godzina wizyty - alternatywny")
	preferred_date_alt2 = models.DateTimeField(null=True, blank=True, help_text="Preferowany dzień i godzina wizyty - alternatywny")
	extra_info = MarkdownField(null=True, help_text="Dodatkowe informacje")
	personal_data_agreement = models.BooleanField(default=True, help_text="Zgoda na przechowywanie i pzetwarzanie danych osobowych w celach umówienia wizyty i w celach marketingowych")
	is_active = models.BooleanField(default=True, help_text="Czy prośba o zapis do dentysty jest nadal aktualna? (nie nastąpił kontakt i umówienie wizyty)")
	office = models.ForeignKey(Office, help_text="Wybierz gabinet", related_name='appointment')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "/office/"

	class Meta:
		verbose_name = "Appointment"
		verbose_name_plural = 'Appointments'

class DentistDay(models.Model):
	date = models.DateField(null=True)
	dentist = models.ForeignKey(Dentist)
	office = models.ForeignKey(Office)
	slot10_11 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1000_1100")
	slot11_12 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1100_1200")
	slot12_13 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1200_1300")
	slot13_14 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1300_1400")
	slot14_15 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1400_1500")
	slot15_16 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1500_1600")
	slot16_17 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1600_1700")
	slot17_18 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1700_1800")
	slot18_19 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1800_1900")
	slot19_20 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1900_2000")

	def __str__(self):
		return  "{}{}".format(self.date, self.dentist.id)

	def get_absolute_url(self):
		return reverse("schedule_detail", kwargs={'pk': self.pk})

	def get_edit_url():
		return reverse("schedule_edit", kwargs={'pk': self.pk})

	class Meta:
		verbose_name = "Schedule"
		verbose_name_plural = 'Schedules'


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
	appointment = models.ForeignKey(Appointment, blank=True, null=True)
	slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/patient/{0}/{1}/".format(self.subject.slug, self.slug)

	def event_type_verbose(self):
		return dict(Event.EVENT_TYPES)[self.event_type]

	class Meta:
		verbose_name = "Event"
		verbose_name_plural = 'Events'