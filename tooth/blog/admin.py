from django_markdown.admin import MarkdownModelAdmin

from django.contrib import admin

from . import models

# Register your models here.

class PostAdmin(MarkdownModelAdmin):
    list_display = ("title", "pub_date",)
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(MarkdownModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}

class TagAdmin(MarkdownModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)