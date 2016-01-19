from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, Group


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=150)
	description = models.TextField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "/shop/category/{0}/".format(self.slug)

	class Meta:
		verbose_name = "Shop Product Category"
		verbose_name_plural = 'Shop Product Categories'


class Tag(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "/shop/tag/{0}/".format(self.slug)

	class Meta:
		verbose_name = "Shop Product Tag"
		verbose_name_plural = 'Shop Product Tags'

class Product(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_photo', blank=True)
    manufacturer = models.CharField(max_length=300, blank=True)
    price_in_PLN = models.DecimalField(max_digits=6, decimal_places=2)
    retail = models.BooleanField(default=True, help_text="Do sprzedaży detalicznej = True, Do sprzedaży hurtowej - False")
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/shop/product/{0}/".format(self.slug)

    class Meta:
        verbose_name = "Shop Product"
        verbose_name_plural = 'Shop Products'

class Purchase(models.Model):
    product = models.ForeignKey(Product)
    purchaser = models.ForeignKey(User)
    time = models.DateTimeField(auto_now_add=True)
    tx = models.CharField(max_length=250)