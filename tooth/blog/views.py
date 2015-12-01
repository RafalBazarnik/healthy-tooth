from django.views import generic
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from . import models
from . import forms

# Create your views here.
class BlogIndex(generic.ListView):
    # queryset = models.Post.objects.all()
    queryset = models.Post.objects.published()
    template_name = "blog.html"
    paginate_by = 5

class PostDetail(SuccessMessageMixin, generic.DetailView):
    model = models.Post
    template_name = "post_detail.html"

class CategoryView(generic.ListView):
    model = models.Category
    paginate_by = 5
    template_name = 'category.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = models.Category.objects.get(slug=slug)
            return models.Post.objects.filter(category=category)
        except models.Category.DoesNotExist:
            return models.Post.objects.none()

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
    paginate_by = 5
    template_name = 'tag.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = models.Tag.objects.get(slug=slug)
            return tag.post_set.all()
        except models.Tag.DoesNotExist:
            return models.Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        try:
            context['tag'] = models.Tag.objects.get(slug=slug)
        except models.Tag.DoesNotExist:
            context['tag'] = None
        return context

def search(request):
    # search by title or text
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    results = models.Post.objects.filter(Q(text__icontains=query) | Q(title__icontains=query))

    pages = Paginator(results, 5)

    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # render result
    return render_to_response('search_result_blog.html',
                              {'page_obj': returned_page,
                               'object_list': returned_page.object_list,
                               'search': query})

@login_required
def post_new(request):
    if not request.user.is_authenticated():
        return redirect('/login')
    else:
        context =RequestContext(request)
        if request.method == "POST":
            form = forms.NewPostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                upload_user = request.user
                is_published = False
                post.save()
                form = forms.NewPostForm()
                messages.add_message(request, messages.SUCCESS, "Twój post został opublikowany! Już niedługo znajdzie się na naszym blogu! Dziękujemy :)")
                return render(request, 'post_new.html', {'form': form}, context)
        else:
            form = forms.NewPostForm()
        return render(request, 'post_new.html', {'form': form}, context)