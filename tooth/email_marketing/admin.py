from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin


# Register your models here.
admin.site.register(models.MarketingEmail)