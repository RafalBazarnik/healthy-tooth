from django.db import models
import datetime
from django.contrib.auth.models import User, Group
from django.core.validators import MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator


# Create your models here.
class MarketingEmail(models.Model):
    SEX = [
        ("F", "kobieta"),
        ("M", "mężczyzna"),
    ]
    email_title = models.CharField(max_length=50, null=True, blank=True)
    email_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    email_city = models.CharField(max_length=100, blank=False, null=False)
    email_city_alt1 = models.CharField(max_length=100, blank=True, null=True)
    email_city_alt2 = models.CharField(max_length=100, blank=True, null=True)
    email_patients_sex = models.CharField(choices=SEX, null=True, blank=True, max_length=2)
    email_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email_title + " " + str(self.email_date)

    def sex_verbose(self):
        return dict(MarketingEmail.SEX)[self.email_patients_sex]

    def get_absolute_url(self):
        return "/email_marketing/emails_detail/{}/".format(self.pk)

    def save(self, *args, **kwargs):
        self.date = datetime.datetime.now()
        super(MarketingEmail, self).save()