from django.shortcuts import render
from django.views import generic
from . import models


# Create your views here.
class ShopIndexView(generic.ListView):
	queryset = models.Product.objects.all()
	template_name = "shop/products_list.html"
	paginate_by = 10
