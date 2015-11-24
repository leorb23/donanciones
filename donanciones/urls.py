"""donanciones URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from juguetes import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

	url(r'^$', views.index),
	url(r'^donacion/$', views.cliente),
	url(r'^log_in/$', views.log_in),
	url(r'^log_out/$', views.log_out),

	url(r'^estado/(\d{1,10})/$', views.estado),
	url(r'^estado/(\d{1,10})/eliminar$', views.estado_eliminar),
	url(r'^estado/listado/$', views.estados),
	url(r'^estado/nuevo$', views.estado_nuevo),
	
	url(r'^donacion/(\d{1,10})/$', views.donacion),
	url(r'^donacion/(\d{1,10})/eliminar$', views.donacion_eliminar),
	url(r'^donacion/listado$', views.donaciones),
	url(r'^donacion/nuevo$', views.donacion_nuevo),
	
	url(r'^donante/(\d{1,10})/$', views.donante),
	url(r'^donante/(\d{1,10})/eliminar$', views.donante_eliminar),
	url(r'^donante/listado$', views.donantes),
	url(r'^donante/nuevo$', views.donante_nuevo),

	url(r'^juguete/(\d{1,10})/$', views.juguete),
	url(r'^juguete/(\d{1,10})/eliminar$', views.juguete_eliminar),
	url(r'^juguete/listado$', views.juguetes),
	url(r'^juguete/nuevo$', views.juguete_nuevo),

	url("", include('social.apps.django_app.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
