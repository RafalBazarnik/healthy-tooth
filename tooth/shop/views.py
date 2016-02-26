from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.db.models import Q
from . import models, forms


class PurchaseFormView(generic.FormView):
    model = models.Purchase
    form_class = forms.PurchaseForm
    template_name = 'shop/new_purchase.html'

    def get_success_url(self):
        return reverse('shop:purchase_list')

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Patients').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PurchaseFormView, self).dispatch(*args, **kwargs)

class PurchaseStatusUpdate(generic.UpdateView):
    model = models.Purchase
    form_class = forms.PurchaseStatusChangeForm
    template_name = 'shop/purchase_status_edit.html'

    def get_success_url(self):
        return reverse('shop:purchase_list')

    def get_context_data(self, **kwargs):
        purchase = self.get_object().pk
        context = super(PurchaseStatusUpdate, self).get_context_data(**kwargs)
        context['purchase_list'] = models.Purchase.objects.filter(id=purchase).order_by('date')
        return context

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PurchaseStatusUpdate, self).dispatch(*args, **kwargs)


class PurchaseListView(generic.ListView):
    queryset = models.Purchase.objects.all()
    template_name = "shop/purchase_list.html"
    paginate_by = 12

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Patients').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PurchaseListView, self).dispatch(*args, **kwargs)


class PurchaseOfficeListView(generic.ListView):
    queryset = models.Purchase.objects.all().order_by('date') 
    template_name = "shop/purchase_list.html"
    paginate_by = 12

    def get_queryset(self):
        object_list = super(PurchaseOfficeListView, self).get_queryset()
        return object_list.filter(status__in=["C","D","E","F","G","H","J"]).order_by('date')

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PurchaseOfficeListView, self).dispatch(*args, **kwargs)


class PurchaseDetailView(generic.DetailView):
    model = models.Purchase
    template_name = 'shop/purchase_detail.html'

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name='Offices').count() == 1 or u.groups.filter(name='Patients').count() == 1, login_url='/forbidden'))
    def dispatch(self, *args, **kwargs):
        return super(PurchaseDetailView, self).dispatch(*args, **kwargs)


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