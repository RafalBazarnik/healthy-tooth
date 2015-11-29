from django_markdown.admin import MarkdownModelAdmin

from django.contrib import admin

from . import models

# Register your models here.

class PatientAdmin(MarkdownModelAdmin):
    list_display = ("name", "surname",)
    prepopulated_fields = {"slug": ("surname","name","pesel",)}

class EventAdmin(MarkdownModelAdmin):
    list_display = ("title", "date", "subject",)
    prepopulated_fields = {"slug": ("title", "event_type", "subject", "dentist",)}

class OfficeAdmin(MarkdownModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name", "office_id",)}

class DentistAdmin(MarkdownModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("surname", "name", "pwz_number",)}

admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Office, OfficeAdmin)
admin.site.register(models.Dentist, DentistAdmin)
# admin.site.register(models.User)