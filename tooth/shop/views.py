from django.shortcuts import render
from django.views import generic
from . import models


# Create your views here.
class ShopIndexView(generic.ListView):
	queryset = models.Product.objects.all()
	template_name = "shop/products_list.html"
	paginate_by = 12

class ProductDetailView(generic.DetailView):
    model = models.Product
    template_name = 'shop/product_detail.html'

class CategoryView(generic.ListView):
    model = models.Category
    paginate_by = 12
    template_name = 'shop/product_category.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = models.Category.objects.get(slug=slug)
            return models.Product.objects.filter(category=category)
        except models.Category.DoesNotExist:
            return models.Product.objects.none()

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        try:
            context['category'] = models.Category.objects.get(slug=slug)
        except models.Category.DoesNotExist:
            context['category'] = None
        return context

class TagView(generic.ListView):
    model = models.Tag
    paginate_by = 12
    template_name = 'shop/product_tag.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = models.Tag.objects.get(slug=slug)
            return tag.product_set.all()
        except models.Tag.DoesNotExist:
            return models.Product.objects.none()

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        try:
            context['tag'] = models.Tag.objects.get(slug=slug)
        except models.Tag.DoesNotExist:
            context['tag'] = None
        return context