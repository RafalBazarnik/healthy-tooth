from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.

class ProductAdmin(MarkdownModelAdmin):
	list_display = ("name",)
	prepopulated_fields = {"slug": ("name", "manufacturer")}

class CategoryAdmin(MarkdownModelAdmin):
	list_display = ("name",)
	prepopulated_fields = {"slug": ("name",)}

class TagAdmin(MarkdownModelAdmin):
	list_display = ("name",)
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
