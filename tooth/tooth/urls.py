"""tooth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from main_page import urls
from shop import urls
from blog import urls


urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^blog', include('blog.urls', namespace='blog')),
    url(r'^shop', include('shop.urls', namespace='shop')),
    url(r'^email_marketing', include('email_marketing.urls', namespace='email_marketing')),
    url(r'^', include('main_page.urls', namespace="main_page")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import handler400, handler403, handler404, handler500

handler400 = 'main_page.views.handler400'
handler403 = 'main_page.views.handler403'
handler404 = 'main_page.views.handler404'
handler500 = 'main_page.views.handler500'