from django.db import models
from django_markdown.models import MarkdownField

from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/category/{0}/".format(self.slug)

    class Meta:
        verbose_name = "Blog Posts Categories"
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/tag/{0}/".format(self.slug)

    class Meta:
        verbose_name = "Blog Posts Tag"
        verbose_name_plural = 'Blog Posts Tags'


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    text = MarkdownField(null=True)
    slug = models.SlugField(max_length=40, unique=True, null=True)
    upload_user = models.ForeignKey(User, null=True)
    office = models.ForeignKey('main_page.Office', null=True, blank=True)
    dentist = models.ForeignKey('main_page.Dentist', null=True, blank=True)
    other_author = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_short_post_text(self):
        short = ""
        sentence_list = self.text.split(".")
        i = 0
        if len(str(self.text)) > 200:
            while len(short) < 200:
                short += sentence_list[i]
                short += '.'
                i += 1
            return short

    def get_absolute_url(self):
        return "/blog/{0}/{1}/{2}/".format(self.pub_date.year, self.pub_date.month, self.slug)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-pub_date"]