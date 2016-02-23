from django.db import models
from django.core.files import File
from django_markdown.models import MarkdownField
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.validators import validate_email
from django.contrib.auth.models import User, Group
from django.utils.text import slugify
from django.core.urlresolvers import reverse
import os
import datetime
from random import randint


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
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Niepoprawny numer telefonu. Powinien mieć minimum 9 i maksymalnie 15 cyfr")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15, help_text="Numer telefonu")
    phone_number_alt = models.CharField(validators=[phone_regex], blank=True, max_length=15, help_text="Alternatywny numer telefonu")
    email = models.EmailField(null=True, help_text="Adres email")
    skype = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True

def get_image_path(instance, filename):
    random = randint(1000, 9999)
    return os.path.join(str(random), str(filename))

class Patient(Contact):
    SEX = [
        ("F", "kobieta"),
        ("M", "mężczyzna"),
    ]
    name = models.CharField(max_length=100, help_text="Imię")
    surname = models.CharField(max_length=100, help_text="Nazwisko")
    pesel = models.CharField(max_length=11, null=True, help_text="Numer PESEL", validators=[MaxLengthValidator(11), MinLengthValidator(11)])
    profile_image = models.ImageField(upload_to="patients", blank=True, null=True, help_text="Zdjęcie")
    sex = models.CharField(choices=SEX, null=True, max_length=20, help_text="Płeć")
    age = models.CharField(null=True, max_length=3, help_text="Wiek")
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True,
                            help_text="Nazwa linku w postaci - nazwisko-imie-pesel - male litery, bez polskich znaków")
    user = models.ForeignKey(User, null=True, blank=True)

    def save(self, *args, **kwargs):
        is_new = self.user is None
        text = self.surname + " " + self.name + " " + self.pesel
        self.slug = slugify(text)
        if is_new:
            password = self.pesel
            user = User.objects.create_user(username=self.slug, first_name=self.name, last_name=self.surname, email=self.email, password=password)
            group = Group.objects.get(name='Patients') 
            group.user_set.add(user)
            user.save()
            user.is_superuser = False
            user.is_staff = False
            user.is_active = True
            self.user = user
        super(Patient, self).save()

    def __str__(self):
        return self.surname + " " + self.name + " " + self.pesel

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
    logo_image = models.ImageField(upload_to="offices", blank=True, null=True, help_text="Logo")
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
    profile_image = models.ImageField(upload_to="dentists", blank=True, null=True, help_text="Zdjęcie")
    pwz_number = models.CharField(max_length=87, null=True, help_text="7-cyfrowy numer prawa wykonywania zawodu (PWZ)",
         validators=[MaxLengthValidator(7), MinLengthValidator(7)])
    specialties = models.CharField(max_length=50, null=True, help_text="Specjalizacja")
    slug = models.SlugField(max_length=40, unique=True, null=True, help_text="Nazwa linku w postaci - nazwisko-imie-pwz - male litery, bez polskich znaków")
    office = models.ForeignKey(Office, null=True, related_name="workplace")

    def __str__(self):
        return self.surname + " " + self.name

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
    slot10_11 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1000_1100", help_text="10:00-11.00")
    slot11_12 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1100_1200", help_text="11:00-12.00")
    slot12_13 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1200_1300", help_text="12:00-13.00")
    slot13_14 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1300_1400", help_text="13:00-14.00")
    slot14_15 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1400_1500", help_text="14:00-15.00")
    slot15_16 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1500_1600", help_text="15:00-16.00")
    slot16_17 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1600_1700", help_text="16:00-17.00")
    slot17_18 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1700_1800", help_text="17:00-18.00")
    slot18_19 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1800_1900", help_text="18:00-19.00")
    slot19_20 = models.ForeignKey(User, null=True, blank=True, related_name="hours_1900_2000", help_text="19:00-20.00")

    def __str__(self):
        return  "{}".format(self.date)

    def get_absolute_url(self):
        return "/schedule/day/{0}/".format(self.pk)

    def get_edit_url(self):
        return "/schedule/day_edit/{0}/".format(self.pk)

    def get_cancel_url(self):
        return "/patient_zone/appointment_cancel/{0}/".format(self.pk)

    def get_signup_url(self):
        return "/patient_zone/appointment_signup/{0}/".format(self.pk)

    @property
    def get_fields_list(self):
        return self._meta.get_fields()
    
    @property
    def is_active(self):
        return (self.date >= datetime.date.today())

    @property
    def get_slots_dict(self):
        slots_dict = {self._meta.get_field('slot10_11').help_text: self.slot10_11,
                      self._meta.get_field('slot11_12').help_text: self.slot11_12, 
                      self._meta.get_field('slot12_13').help_text: self.slot12_13, 
                      self._meta.get_field('slot13_14').help_text: self.slot13_14, 
                      self._meta.get_field('slot14_15').help_text: self.slot14_15, 
                      self._meta.get_field('slot15_16').help_text: self.slot15_16, 
                      self._meta.get_field('slot16_17').help_text: self.slot16_17, 
                      self._meta.get_field('slot17_18').help_text: self.slot17_18, 
                      self._meta.get_field('slot18_19').help_text: self.slot18_19, 
                      self._meta.get_field('slot19_20').help_text: self.slot19_20}
        return slots_dict

    @property
    def get_free_slots_dict(self):
        slots_dict = {self._meta.get_field('slot10_11').help_text: self.slot10_11,
                      self._meta.get_field('slot11_12').help_text: self.slot11_12, 
                      self._meta.get_field('slot12_13').help_text: self.slot12_13, 
                      self._meta.get_field('slot13_14').help_text: self.slot13_14, 
                      self._meta.get_field('slot14_15').help_text: self.slot14_15, 
                      self._meta.get_field('slot15_16').help_text: self.slot15_16, 
                      self._meta.get_field('slot16_17').help_text: self.slot16_17, 
                      self._meta.get_field('slot17_18').help_text: self.slot17_18, 
                      self._meta.get_field('slot18_19').help_text: self.slot18_19, 
                      self._meta.get_field('slot19_20').help_text: self.slot19_20}
        free_slots_dict = {}
        for name, slot in slots_dict.items():
            if slot is not None:
                if slot.groups.all():
                    if slot.groups.all()[0].name == "Offices":
                        free_slots_dict.update({name: slot})
        return free_slots_dict
    

    @property
    def has_free_slots(self):
        slots_list = [self.slot10_11, self.slot11_12, self.slot12_13, self.slot13_14, self.slot14_15, self.slot15_16, self.slot16_17, self.slot17_18, self.slot18_19, self.slot19_20]
        for slot in slots_list:
            if slot is not None:
                if slot.groups.all():
                    if slot.groups.all()[0].name == "Offices" and (self.date >= datetime.date.today()):
                        return True
        return False

    class Meta:
        unique_together = ('date', 'dentist',)
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
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def __str__(self):
        return self.title + str(self.date)

    def get_absolute_url(self):
        return "/patient/event/{0}/".format(self.slug)

    def event_type_verbose(self):
        return dict(Event.EVENT_TYPES)[self.event_type]

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = 'Events'

    def save(self, *args, **kwargs):
        slug_string = "{0} {1} {2} {3}".format(self.title, self.event_type, self.subject, str(self.date)) 
        self.slug = slugify(slug_string)
        super(Event, self).save()