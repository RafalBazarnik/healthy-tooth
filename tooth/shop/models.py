from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.contrib.auth.models import User, Group
import main_page


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
        return "'" + self.name + "'" + " firmy: " + self.manufacturer + " cena: " + str(self.price_in_PLN) + " PLN"

    def get_absolute_url(self):
        return "/shop/product/{0}/".format(self.slug)

    class Meta:
        verbose_name = "Shop Product"
        verbose_name_plural = 'Shop Products'

class Purchase(models.Model):
    STATUSES = [
        ("A", "zamówione"),
        ("B", "opłacone"),
        ("C", "zwrócone"),
        ("D", "reklamacja"),
        ("E", "potwierdzone"),
        ("F", "wysłane"),
        ("G", "gotowe do odbioru"),
        ("H", "odebrane"),
        ("I", "nieopłacone"),
        ("J", "nieodebrane"),
    ]
    product_1 = models.ForeignKey(Product, null=True, blank=True, related_name='product_slot_1')
    quantity_1 = models.PositiveIntegerField(null=True, blank=True, default=1)
    product_2 = models.ForeignKey(Product, null=True, blank=True, related_name='product_slot_2')
    quantity_2 = models.PositiveIntegerField(null=True, blank=True, default=1)
    product_3 = models.ForeignKey(Product, null=True, blank=True, related_name='product_slot_3')
    quantity_3 = models.PositiveIntegerField(null=True, blank=True, default=1)
    product_4 = models.ForeignKey(Product, null=True, blank=True, related_name='product_slot_4')
    quantity_4 = models.PositiveIntegerField(null=True, blank=True, default=1)
    product_5 = models.ForeignKey(Product, null=True, blank=True, related_name='product_slot_5')
    quantity_5 = models.PositiveIntegerField(null=True, blank=True, default=1)
    purchaser = models.ForeignKey(User)
    office = models.ForeignKey(main_page.models.Office, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    status = models.CharField(choices=STATUSES, null=True, blank=True, max_length=20)
    additional_info = models.CharField(max_length=250)
    purchase_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.purchaser.username + " " + str(self.date)

    def status_verbose(self):
        return dict(Purchase.STATUSES)[self.status]

    def get_absolute_url(self):
        return "/shop/purchase/{0}/".format(self.pk)

    def get_edit_url(self):
        return "/shop/office/purchase/update/{0}/".format(self.pk)

    def calculate_total_price(self):
        total_price = 0
        list_of_products = [
            (self.product_1, self.quantity_1),
            (self.product_2, self.quantity_2),
            (self.product_3, self.quantity_3),
            (self.product_4, self.quantity_4),
            (self.product_5, self.quantity_5),
            ]
        for product in list_of_products:
            if product[0]:
                total_price += product[0].price_in_PLN * product[1]
        return total_price

    def save(self, *args, **kwargs):
        if self.total_price is None:
            self.total_price = self.calculate_total_price()
            self.status = "A"
            purchase_id_text = '{} {}'.format(str(self.total_price), str(self.date))
            self.purchase_id = slugify(purchase_id_text)
        super(Purchase, self).save()
